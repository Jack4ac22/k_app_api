from fastapi import APIRouter, Depends
from db.database import get_db
from schemas import person_schemas
from sqlalchemy.orm.session import Session
from db import db_person
from typing import List

from fastapi import APIRouter
router = APIRouter(
    prefix="/person",
    tags=["person"]
)


@router.post("", response_model=person_schemas.PersonDisplay)
def create_new_person(request: person_schemas.PersonBase, db: Session = Depends(get_db)):
    return db_person.create_person(request, db)


@router.get('/all', response_model=List[person_schemas.PersonDisplay])
def get_all_persons(db: Session = Depends(get_db)):
    return db_person.get_all(db)
