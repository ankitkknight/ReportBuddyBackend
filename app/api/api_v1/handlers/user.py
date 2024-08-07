from fastapi import APIRouter
from app.schemas.user_schema import UserAuth, UserOut, UserLogin
from app.services.user_service import UserService
from fastapi import APIRouter, HTTPException, status
from app.core.security import create_access_token, create_refresh_token
import pymongo


user_router = APIRouter()

@user_router.post("/signup", summary="signup a new user", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(data: UserAuth):
    try:
       created_user = await UserService.create_user(data)
       return created_user
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )
    

@user_router.post("/login", summary="login user")
async def login_user(data: UserLogin):
    user = await UserService.authenticate(email=data.email, password=data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
    }

    