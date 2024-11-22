from fastapi import APIRouter, HTTPException, Request

from database.postgres import User
from database.schemas import UserOutSchema, UserUpdateSchema


router = APIRouter()


@router.get("/me", response_model=UserOutSchema)
async def get_me(request: Request):
    user = request.state.user
    if not user:
        raise HTTPException(400, "You are not logged in")
    return user


@router.post("/me", response_model=UserOutSchema)
async def post_me(request: Request, user_in: UserUpdateSchema):
    logged_user = request.state.user
    if not logged_user:
        raise HTTPException(400, "You are not logged in")
    if user_in.email == logged_user.email and user_in.name == logged_user.name:
        raise HTTPException(400, "Email and name is absolutely the same as provided")
    if user_in.email != logged_user.email and await User.check_email_exists(user_in.email):
        raise HTTPException(400, "This email is already in use of another account.")
    logged_user.email = user_in.email
    logged_user.name = user_in.name 
    await logged_user.save()
    return logged_user
    
    

        