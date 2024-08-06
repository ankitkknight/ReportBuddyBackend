from fastapi import APIRouter
from app.schemas.user_schema import UserAuth, UserOut
from app.services.user_service import UserService
from fastapi import APIRouter, HTTPException, status
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
    

@user_router.post("/login", summary="login user", response_model=UserOut)
async def login_user(data: UserAuth):
    user = await UserService.authenticate(email=data.email, password=data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    return user

    