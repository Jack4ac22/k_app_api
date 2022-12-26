from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
import enum
from schemas import personalized_enums, user_schemas, person_schemas


class PhoneBase(BaseModel):
    person_id: int = 1
    phone: str = "+352671536358"
    description: str = "personal"


class PhoneDisplay(PhoneBase):
    id: int
    created_at: datetime
    updated_at: datetime
    person: person_schemas.PersonDisplay

    class Config:
        orm_mode = True
