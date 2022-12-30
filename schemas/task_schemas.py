from datetime import datetime
from pydantic import BaseModel
from schemas import personalized_enums
from typing import List, Union
import enum


class TaskBase(BaseModel):
    person_id: int
    title: str
    content: str
    task_status: personalized_enums.Task_status


class TaskDisplay(BaseModel):
    id: int
    person_id: int
    title: str
    content: str
    created_at: datetime
    updated_at: Union[datetime, None]
    task_status: enum.Enum

    class Config:
        orm_mode = True
