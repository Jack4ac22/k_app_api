from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
import enum
from schemas import personalized_enums, user_schemas, person_schemas


class PersonInPhones(BaseModel):
    id: int
    first_name: str = "John"
    last_name: str = "Doe"
    gender: enum.Enum
    email: EmailStr = "J_Doe@gmail.com"

    class Config:
        orm_mode = True


class PhoneBase(BaseModel):
    person_id: int = 1
    phone: str = "+352671536358"
    description: str = "personal"


class PhoneDisplay(PhoneBase):
    id: int
    created_at: datetime
    updated_at: datetime
    person: PersonInPhones

    class Config:
        orm_mode = True
