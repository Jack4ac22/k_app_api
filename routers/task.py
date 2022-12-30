from schemas import task_schemas
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_task, db_check_methods

router = APIRouter(
    prefix="/task",
    tags=["task"]
)


@router.post("")
def create_new_task(request: task_schemas.TaskBase, db: Session = Depends(get_db)):
    return db_task.create_new(request, db)
