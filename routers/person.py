from fastapi import APIRouter, Depends, status
from db.database import get_db
from schemas import person_schemas
from sqlalchemy.orm.session import Session
from db import db_person
from typing import List
from pydantic import EmailStr
from utilities import jwt_manager

router = APIRouter(
    prefix="/person",
    tags=["person"]
)


@router.post("", response_model=person_schemas.PersonDisplaySimple, status_code=status.HTTP_201_CREATED)
def create_new_person(request: person_schemas.PersonBase, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    print(user_id)
    return db_person.create_person(request, db, user_id)


@router.get("/all", response_model=List[person_schemas.PersonDisplay])
def get_all_persons(db: Session = Depends(get_db)):
    return db_person.get_all(db)


@router.get("/id{id}", response_model=person_schemas.PersonDisplay)
def get_person_by_id(id: int, db: Session = Depends(get_db)):
    return db_person.get_by_id(id, db)


@router.get("/email{email}", response_model=person_schemas.PersonDisplay)
def get_person_by_id(email: EmailStr, db: Session = Depends(get_db)):
    return db_person.get_by_email(email, db)


@router.put("{id}", response_model=person_schemas.PersonDisplay)
def update_person(id: int, request: person_schemas.PersonBase, db: Session = Depends(get_db)):
    return db_person.update(id, request, db)


@router.delete("/{id]", response_model=person_schemas.PersonDisplaySimple)
def delete_person(id: int, db: Session = Depends(get_db)):
    return db_person.delete_by_id(id, db)
