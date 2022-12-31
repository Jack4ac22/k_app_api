from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas import person_job_title_schemas
from .models import DbPersonJob
from db.db_job_title import check_job_title_id
from db.db_check_methods import check_person_id


def create_person_job_title(request: person_job_title_schemas.PersonTitleBase, db: Session):
    check_person_id(request.person_id, db)
    check_job_title_id(request.title_id, db)
    new_person_title = DbPersonJob(**request.dict())
    db.add(new_person_title)
    db.commit()
    db.refresh(new_person_title)
    return new_person_title
