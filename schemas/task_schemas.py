from datetime import datetime
from pydantic import BaseModel, EmailStr
from schemas import personalized_enums
from typing import List, Union
import enum


class PersonInTasks(BaseModel):
    id: int
    first_name: str = "John"
    last_name: str = "Doe"
    gender: enum.Enum
    email: EmailStr = "J_Doe@gmail.com"

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    person_id: int = 1
    title: str
    content: str
    task_status: personalized_enums.Task_status


class TaskDisplay(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: Union[datetime, None]
    task_status: enum.Enum
    person: PersonInTasks

    class Config:
        orm_mode = True


class TaskDisplaySimple(BaseModel):
    id: int
    person_id: int
    title: str
    content: str
    created_at: datetime
    updated_at: Union[datetime, None]
    task_status: enum.Enum

    class Config:
        orm_mode = True
