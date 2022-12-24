from datetime import datetime, date, time
from pydantic import BaseModel, EmailStr
from schemas import personalized_enums
from typing import Optional
import enum
from typing import List


class PersonBase(BaseModel):
    first_name: str = "John"
    last_name: str = "Doe"
    gender: personalized_enums.Genders_person
    email: EmailStr = "J_Doe@gmail.com"
    birthday: date = "1900-12-31"
    added_by: int = 1


class PersonDisplay(PersonBase):
    id: int
    first_name: str = "John"
    last_name: str = "Doe"
    gender: enum.Enum
    email: EmailStr = "J_Doe@gmail.com"
    birthday: date
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
