from pydantic import BaseModel, EmailStr
from .user import UserResponse


class TokenRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    user: UserResponse
    token: str
