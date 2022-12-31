from db import db_job_title
from db.database import get_db
from fastapi import APIRouter, Depends, status
from schemas import job_title_schemas
from sqlalchemy.orm.session import Session
from typing import List
from utilities import jwt_manager

router = APIRouter(
    prefix="/job_title",
    tags=["Job titles"]
)


@router.post("", response_model=job_title_schemas.JobTitleDisplay, status_code=status.HTTP_201_CREATED)
def create_new_job_title(request: job_title_schemas.JobTitleBase, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_job_title.create_job_title(request, db, user_id)


@router.get("/all", response_model=List[job_title_schemas.JobTitleDisplay])
def gett_all_job_titles(db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_job_title.get_all(db)


@router.get("my_all", response_model=List[job_title_schemas.JobTitleDisplay])
def get_all_user_job_titles(db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_job_title.get_all_user(user_id, db)


# TODO: add verification later... testing back_puopulates in many_to_many
@router.get("/{id}", response_model=job_title_schemas.JobTitleDisplay)
def get_job_title_by_id(id: int, db: Session = Depends(get_db)):
    return db_job_title.get_one_by_id(id, db)
