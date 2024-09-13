from fastapi import APIRouter, HTTPException, Request, Response

import asyncio
from concurrent.futures import ProcessPoolExecutor

from database.schemas import UserInSchema, UserOutSchema
from database.postgres import User
from utils.exceptions import UsernameAlreadyTakenError
from utils.password import hash_password, verify_password
import conf


router = APIRouter()


@router.post("/register", response_model=UserOutSchema, status_code=201)
async def register(user_in: UserInSchema):
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
async def login(user_in: UserInSchema, response: Response):
    user = await User.get_by_username(username=user_in.username)
    if not user:
        raise HTTPException(404, "User with provided username not found")
    if not verify_password(user.password, user_in.password):  # type: ignore
        raise HTTPException(400, "Password not correct")
    response.set_cookie(
        key="session_id",
        value=user.username,  # type: ignore
        max_age=3600,
        domain=conf.DOMAIN_NAME,
        secure=(not conf.TESTING),
        httponly=True,
        samesite="strict"
    )
    return {
        "result": "success"
    }


@router.get("/me")
async def get_me(request: Request):
    cookie_username = request.cookies.get("auth")
    if not cookie_username:
        raise HTTPException(400, "You are not logged in")
    return {
        "name": cookie_username
    }


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(
        "session_id",
        domain=conf.DOMAIN_NAME,
        secure=(not conf.TESTING),
        httponly=True,
        samesite="strict"
    )
    