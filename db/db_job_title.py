from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas import job_title_schemas
from .models import DbJobTitle
from db import db_check_methods


def check_title_duplication(user_id: int, job_title: str, db: Session):
    targeted_job_title = db.query(DbJobTitle).filter(
        DbJobTitle.title == job_title)
    if targeted_job_title.first():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"The job title: '{job_title}' is already used, please verify."
        )
    return targeted_job_title


def check_job_title_id(id: int, db: Session):
    job_title = db.query(DbJobTitle).filter(DbJobTitle.id == id)
    if not job_title.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding job_title was found with ID: {id}, please verify the ID and try again."
        )
    return job_title


def create_job_title(request: job_title_schemas.JobTitleBase, db: Session, user_id: int):
    check_title_duplication(user_id, request.title, db)
    new_job_title = DbJobTitle(
        title=request.title,
        description=request.description
    )
    db.add(new_job_title)
    db.commit()
    db.refresh(new_job_title)
    print(new_job_title)
    return new_job_title


def get_all(db: Session):
    return db.query(DbJobTitle).all()


def get_one_by_id(id: int, db: Session):
    return check_job_title_id(id, db).first()


def update(id: int, request: job_title_schemas.JobTitleBase, db: Session):
    targeted_job_title = check_job_title_id(id, db)
    targeted_job_title.update(request.dict())
    db.commit()
    return targeted_job_title.first()


def delete(id: int, db: Session):
    targeted_job_title = check_job_title_id(id, db)
    deleted_job_title = targeted_job_title.first()
    targeted_job_title.delete()
    db.commit()
    return deleted_job_title
