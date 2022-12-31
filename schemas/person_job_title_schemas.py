from datetime import datetime
from pydantic import BaseModel, EmailStr
from schemas import personalized_enums
from typing import List, Union, Optional
import enum


class PersonInPT(BaseModel):
    id: int
    first_name: str = "John"
    last_name: str = "Doe"
    gender: enum.Enum
    email: EmailStr = "J_Doe@gmail.com"

    class Config:
        orm_mode = True


class TitleInPT(BaseModel):
    id: int
    title: str
    description: Union[str, None]

    class Config:
        orm_mode = True


class PersonTitleBase(BaseModel):
    person_id: int
    title_id: int


class PersonTitleDisplay(BaseModel):
    id: int
    person_id: int
    title_id: int
    created_at: datetime
    update_at: Union[datetime, None]
    person: PersonInPT
    job_title: TitleInPT

    class Config:
        orm_mode = True


class PersonTitleDisplayInTitle(BaseModel):
    id: int
    created_at: datetime
    update_at: Union[datetime, None]
    person: PersonInPT

    class Config:
        orm_mode = True


class PersonTitleDisplayInPerson(BaseModel):
    id: int
    created_at: datetime
    update_at: Union[datetime, None]
    job_title: TitleInPT

    class Config:
        orm_mode = True
