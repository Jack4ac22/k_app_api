from datetime import datetime
from pydantic import BaseModel, EmailStr
from schemas import personalized_enums
from typing import List, Union, Optional
import enum



class JobTitleBase(BaseModel):
    title: str
    description: Optional[str]


class JobTitleDisplay(JobTitleBase):
    id: int = 1
    created_at: datetime
    update_at: Union[datetime, None]
    added_by: int = 1

    class Config:
        orm_mode = True
