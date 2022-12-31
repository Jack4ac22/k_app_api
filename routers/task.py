from schemas import task_schemas
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_task
from typing import List
from utilities import jwt_manager

router = APIRouter(
    prefix="/task",
    tags=["task"]
)


@router.post("", response_model=task_schemas.TaskDisplay, status_code=status.HTTP_201_CREATED)
def create_new_task(request: task_schemas.TaskBase, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_task.create_new(request, db)


@router.get("/all", response_model=List[task_schemas.TaskDisplay])
def get_all_tasks(db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_task.get_all(db)


@router.get("/task{task_id}", response_model=task_schemas.TaskDisplay)
def get_single_task_by_id(task_id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_task.get_task_by_id(task_id, db)


@router.get("per{person_id}", response_model=List[task_schemas.TaskDisplaySimple])
def get_all_tasks_for_person(person_id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_task.get_personal_tasks(person_id, db)


@router.put("{id}", response_model=task_schemas.TaskDisplay)
def update_task(id: int, request: task_schemas.TaskBase, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_task.update(id, request, db)


@router.put("/open{id}", response_model=task_schemas.TaskDisplay)
def task_status_open(id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_task.status_open(id, db)


@router.put("/close{id}", response_model=task_schemas.TaskDisplay)
def task_status_close(id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_task.status_close(id, db)


@router.put("/standby{id}", response_model=task_schemas.TaskDisplay)
def task_status_standby(id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_task.status_standby(id, db)


@router.delete("/{id}", response_model=task_schemas.TaskDisplaySimple)
def delete_task(id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_task.delete(id, db)
