from db import db_peron_job_title
from db.database import get_db
from fastapi import APIRouter, Depends, status
from schemas import person_job_title_schemas
from sqlalchemy.orm.session import Session
from typing import List, Union
from utilities import jwt_manager


router = APIRouter(
    prefix="/person_job_title",
    tags=["Person - Job title"]
)


@router.post("", response_model=person_job_title_schemas.PersonTitleDisplay, status_code=status.HTTP_201_CREATED)
def create_new_person_job_title(request: person_job_title_schemas.PersonTitleBase, db: Session = Depends(get_db)):
    return db_peron_job_title.create_person_job_title(request, db)
