from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional


class UserLogin(BaseModel):
    email: str
    password: str

class UserAuth(BaseModel):
    first_name: str = Field(..., description="User first name")
    last_name: str = Field(..., description="User last name")
    email: EmailStr = Field(..., description="User email")
    phone_number: str = Field(..., description="User phone number")
    password: str = Field(...,min_length=5, description="user password")


class UserOut(BaseModel):
    user_id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str


