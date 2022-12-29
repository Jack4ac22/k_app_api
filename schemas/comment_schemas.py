from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional, Union
import enum


class PersonInComments(BaseModel):
    id: int
    first_name: str = "John"
    last_name: str = "Doe"
    gender: enum.Enum = "male"
    email: EmailStr = "J_Doe@gmail.com"

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    persn_id: int = 1
    title: str = "comment title"
    content: str = "comment content"


class CommentDisplay(CommentBase):
    created_at: datetime
    updated_at: Union[datetime, None]
    person: PersonInComments

    class Config:
        orm_mode = True


class CommentDisplaySimple(CommentBase):
    created_at: datetime
    updated_at: Union[datetime, None]

    class Config:
        orm_mode = True
