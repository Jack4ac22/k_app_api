from datetime import datetime, date, time
from pydantic import BaseModel, EmailStr
from schemas import personalized_enums, person_job_title_schemas
from typing import List, Union
from typing import Optional
import enum


class PhoneInPerson(BaseModel):
    id: int
    phone: str = "+352671536358"
    description: str = "personal"

    class Config:
        orm_mode = True


class CommentInPerson(BaseModel):
    id: int
    title: str = "comment's title"
    content: str = "comment's content"

    class Config:
        orm_mode = True


class TaskInPerson(BaseModel):
    id: int
    title: str = "task's title"
    content: str = "task's content"
    task_status: enum.Enum = "open / closed / other"

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
    gender: enum.Enum = "male/femail"
    email: EmailStr = "J_Doe@gmail.com"
    birthday: date
    created_at: datetime
    updated_at: Union[datetime, None]
    added_by: int
    phones: Union[List[PhoneInPerson], None]
    comments: Union[List[CommentInPerson], None]
    tasks: Union[List[TaskInPerson], None]
    job_titles:Union[List[person_job_title_schemas.PersonTitleDisplayInPerson],None]

    class Config:
        orm_mode = True


class PersonDisplaySimple(PersonBase):
    id: int
    first_name: str = "John"
    last_name: str = "Doe"
    gender: enum.Enum = "male/femail"
    email: EmailStr = "J_Doe@gmail.com"
    birthday: date
    created_at: datetime

    class Config:
        orm_mode = True
