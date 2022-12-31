from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas import task_schemas, personalized_enums
from .models import DbTask
from db import db_check_methods


def check_task_id(id: int, db: Session):
    task = db.query(DbTask).filter(DbTask.id == id)
    if not task.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding task was found with ID: {id}, please verify the ID and try again."
        )
    return task


def create_new(request: task_schemas.TaskBase, db: Session):
    db_check_methods.check_person_id(request.person_id, db)
    new_task = DbTask(**request.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    print(new_task)
    return new_task


def get_all(db: Session):
    return db.query(DbTask).all()


def get_task_by_id(task_id: int, db: Session):
    targeted_task = check_task_id(task_id, db)
    return targeted_task.first()


def get_personal_tasks(person_id: int, db: Session):
    db_check_methods.check_person_id(person_id, db)
    tasks = db.query(DbTask).filter(
        DbTask.person_id == person_id).all()
    if not tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding comments were found for the person of ID: {person_id}, please verify and try again."
        )
    return tasks


def update(id: int, request: task_schemas.TaskBase, db: Session):
    targeted_task = check_task_id(id, db)
    targeted_task.update(request.dict())
    db.commit()
    return targeted_task.first()


def status_open(id: int, db: Session):
    targeted_task = check_task_id(id, db)
    data_to_update = dict(task_status="task_open")
    targeted_task.update(data_to_update)
    return targeted_task.first()


def status_close(id: int, db: Session):
    targeted_task = check_task_id(id, db)
    data_to_update = dict(task_status="task_close")
    targeted_task.update(data_to_update)
    return targeted_task.first()


def status_standby(id: int, db: Session):
    targeted_task = check_task_id(id, db)
    data_to_update = dict(task_status="task_standby")
    targeted_task.update(data_to_update)
    return targeted_task.first()


def delete(id: int, db: Session):
    targeted_task = check_task_id(id, db)
    deleted_task = targeted_task.first()
    targeted_task.delete()
    db.commit()
    return deleted_task
