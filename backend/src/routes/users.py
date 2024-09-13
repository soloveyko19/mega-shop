from fastapi import APIRouter, HTTPException, Request, Response

import asyncio
from concurrent.futures import ProcessPoolExecutor

from database.schemas import UserInSchema, UserOutSchema
from database.postgres import User
from database.redis import session_storage
from utils.exceptions import UsernameAlreadyTakenError
from utils.password import hash_password, verify_password
import conf
from utils.session import generate_session_id


router = APIRouter()


@router.post("/register", response_model=UserOutSchema, status_code=201)
async def register(user_in: UserInSchema, request: Request):
    if request.state.user: 
        raise HTTPException(400, "You are already logged in.")
    try:
        await User.check_username_available(user_in.username)
    except UsernameAlreadyTakenError:
        raise HTTPException(400, "This username already taken")
    
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        hashed_password = await loop.run_in_executor(pool, hash_password, user_in.password)

    user = User(
        username=user_in.username,
        password=hashed_password
    )
    await user.save()

    return user
        


@router.post("/login")
async def login(user_in: UserInSchema, response: Response, request: Request):
    if request.state.user:
        raise HTTPException(409, "You are already logged in")
    
    user = await User.get_by_username(username=user_in.username)

    if not user or not verify_password(str(user.password), user_in.password):
        raise HTTPException(400, "Incorrect username or password. Check credentials and try again.")
    
    session_id = await generate_session_id()

    response.set_cookie(
        key="session_id",
        value=session_id,  
        max_age=604800,
        secure=(not conf.TESTING),
        httponly=True,
        samesite="strict"
    )
    await session_storage.set(
        name=session_id,
        value=str(user.username),
        ex=604800,
    )

    return {"result": "success"}


@router.get("/me", response_model=UserOutSchema)
async def get_me(request: Request):
    user = request.state.user
    if not user:
        raise HTTPException(400, "You are not logged in")
    return user


@router.post("/logout")
async def logout(request: Request, response: Response):
    user = request.state.user
    session_id = request.state.session_id
    if not user:
        raise HTTPException(400, f"You are not logged in")
    await session_storage.delete(session_id)
    response.delete_cookie(
        key="session_id"
    )
    return {"result": "success"}
    