from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: int
    created_at: int
    updated_at: int
    first_name: str
    last_name: str
    email: EmailStr


class UserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
