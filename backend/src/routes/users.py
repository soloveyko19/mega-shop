from typing import Optional
from fastapi import APIRouter, HTTPException, Request, Response, Query
import httpx

import asyncio
from concurrent.futures import ProcessPoolExecutor
import uuid

from database.schemas import UserInSchema, UserOutSchema
from database.postgres import User
from database.redis import session_storage
from utils.password import hash_password, verify_password
import conf
from utils.session import generate_session_id


router = APIRouter()


@router.post("/register", response_model=UserOutSchema, status_code=201)
async def register(user_in: UserInSchema, request: Request):
    if request.state.user: 
        raise HTTPException(400, "You are already logged in.")
    if await User.check_email_exists(user_in.email):
        raise HTTPException(400, "This email already taken")
    
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        hashed_password = await loop.run_in_executor(pool, hash_password, user_in.password)

    user = User(
        email=user_in.email,
        password=hashed_password
    )
    await user.save()

    return { "result": "success" }
        

@router.post("/login")
async def login(user_in: UserInSchema, response: Response, request: Request):
    if request.state.user:
        raise HTTPException(409, "You are already logged in")
    
    user = await User.get_by_email(email=user_in.email)

    if not user or not verify_password(str(user.password), user_in.password):
        raise HTTPException(400, "Incorrect username or password. Check credentials and try again.")
    
    session_id = generate_session_id()

    response.set_cookie(
        key="session_id",
        value=session_id,  
        max_age=604800,
        secure=True,
        httponly=True,
        samesite="none" if conf.TESTING else "strict"
    )
    await session_storage.set(
        name=session_id,
        value=str(user.email),
        ex=604800,
    )

    return { "result": "success" }


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


@router.get('/login/google/url')
async def get_login_google_url():
    scope = ['email', 'profile', 'openid']
    url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={conf.GOOGLE_AUTH_CLIENT_ID}&redirect_uri={conf.GOOGLE_AUTH_REDIRECT_URI}&response_type=code&scope={' '.join(scope)}"
    return { "url": url }
    

@router.get('/login/google')
async def get_login_google(response: Response, request: Request, code: Optional[str] = None, error: Optional[str] = None):
    if request.state.user:
        raise HTTPException(400, "You are already logged in")
    if not code and not error:
        raise HTTPException(400)
    elif error:
        raise HTTPException(400, error)
    elif code:
        async with httpx.AsyncClient() as client:
            data = {
                'client_id': conf.GOOGLE_AUTH_CLIENT_ID,
                'client_secret': conf.GOOGLE_AUTH_CLIENT_SECRET,
                'code': code,
                'grant_type': 'authorization_code',
                'redirect_uri': conf.GOOGLE_AUTH_REDIRECT_URI
            }
            resp = await client.post(
                url='https://oauth2.googleapis.com/token',
                data=data
            )
            if resp.status_code != 200:
                raise HTTPException(400, 'Error on athorization through google')
            access_data = resp.json()
            user_info_response = await client.get(
                url='https://www.googleapis.com/oauth2/v3/userinfo',
                headers={
                    "Authorization": f"Bearer {access_data.get('access_token')}"
                }
            )
        if user_info_response.status_code != 200:
            raise HTTPException(400, 'Error on athorization through google')
        user_info = user_info_response.json()
        if not user_info.get('email_verified'):
            raise HTTPException(400, 'Your email must be verified to log in through google')
        if await User.check_email_exists(email=user_info.get('email')):
            session_id = generate_session_id()

            response.set_cookie(
                key="session_id",
                value=session_id,  
                max_age=604800,
                secure=True,
                httponly=True,
                samesite="none" if conf.TESTING else "strict"
            )
            await session_storage.set(
                name=session_id,
                value=user_info.get('email'),
                ex=604800,
            )

            return { "result": "success" }
        else:
            loop = asyncio.get_running_loop()
            with ProcessPoolExecutor() as pool:
                hashed_password = await loop.run_in_executor(pool, hash_password, str(uuid.uuid4()))

            user = User(
                email=user_info.get('email'),
                password=hashed_password,
                name=user_info.get('name')
            )
            await user.save()

            session_id = generate_session_id()

            response.set_cookie(
                key="session_id",
                value=session_id,  
                max_age=604800,
                secure=True,
                httponly=True,
                samesite="none" if conf.TESTING else "strict"
            )
            await session_storage.set(
                name=session_id,
                value=str(user.email),
                ex=604800,
            )

            return { "result": "success" }


    

        