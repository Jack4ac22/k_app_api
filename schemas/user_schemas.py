from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
import enum
from schemas import personalized_enums


class UserBase(BaseModel):
    username: str = "username"
    password: str = "password"
    secret_password: str = "secret_password"
    email: EmailStr


class UserDisplay(BaseModel):
    id: int
    username: str = "username"
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
