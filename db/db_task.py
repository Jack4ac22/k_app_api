from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from schemas import task_schemas, personalized_enums
from .models import DbTask


def create_new(request: task_schemas.TaskBase, db: Session):
    new_task = DbTask(**request.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    print(new_task)
    return new_task
