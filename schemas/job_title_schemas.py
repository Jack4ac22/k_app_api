from datetime import datetime
from pydantic import BaseModel, EmailStr
from schemas import personalized_enums, person_job_title_schemas
from typing import List, Union, Optional
import enum


class JobTitleBase(BaseModel):
    title: str
    description: Optional[str]


class JobTitleDisplay(JobTitleBase):
    id: int = 1
    created_at: datetime
    update_at: Union[datetime, None]
    people: Union[List[person_job_title_schemas.PersonTitleDisplayInTitle], None]

    class Config:
        orm_mode = True


class JobTitleDisplaySimple(BaseModel):
    id: int = 1
    title: str
    description: Optional[str]
    created_at: datetime
    update_at: Union[datetime, None]

    class Config:
        orm_mode = True
