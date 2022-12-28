from datetime import datetime, date, time
from pydantic import BaseModel, EmailStr
from schemas import personalized_enums, phone_schemas
from typing import List, Union
from typing import Optional
import enum


class PhoneInPerson(BaseModel):
    id: int
    phone: str = "+352671536358"
    description: str = "personal"

    class Config:
        orm_mode = True


class PersonBase(BaseModel):
    first_name: str = "John"
    last_name: str = "Doe"
    gender: personalized_enums.Genders_person
    email: EmailStr = "J_Doe@gmail.com"
    birthday: date = "1900-12-31"


class PersonDisplay(BaseModel):
    id: int
    first_name: str = "John"
    last_name: str = "Doe"
    gender: enum.Enum
    email: EmailStr = "J_Doe@gmail.com"
    birthday: date
    created_at: datetime
    updated_at: Union[datetime, None]
    added_by: int
    phones: Union[List[PhoneInPerson], None]

    class Config:
        orm_mode = True


class PersonDisplaySimple(PersonBase):
    id: int
    first_name: str = "John"
    last_name: str = "Doe"
    gender: enum.Enum
    email: EmailStr = "J_Doe@gmail.com"
    birthday: date
    created_at: datetime

    class Config:
        orm_mode = True
