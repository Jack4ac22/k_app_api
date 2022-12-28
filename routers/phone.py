from fastapi import APIRouter, Depends, status
from db.database import get_db
from schemas import phone_schemas
from sqlalchemy.orm.session import Session
from db import db_phone
from typing import List
from utilities import jwt_manager

router = APIRouter(
    prefix="/phone",
    tags=["phone"]
)


@router.post("", response_model=phone_schemas.PhoneDisplay, status_code=status.HTTP_201_CREATED)
def create_new_phone(request: phone_schemas.PhoneBase, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_phone.create_phone(request, db)


@router.get("/all", response_model=List[phone_schemas.PhoneDisplay])
def get_all_phones(db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_phone.get_all(db)


@router.get("/ph{id}", response_model=phone_schemas.PhoneDisplay)
def get_phone_by_id(id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_phone.get_by_id(id, db)


@router.get("/nb{nb}", response_model=List[phone_schemas.PhoneDisplay])
def get_phone_by_number(nb: str, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_phone.get_by_number(nb, db)


@router.put("{id}", response_model=phone_schemas.PhoneDisplay)
def update_phone(id: int, request: phone_schemas.PhoneBase, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_phone.update(id, request, db)


@router.delete("/{id]", response_model=phone_schemas.PhoneDisplaySimple)
def delete_phone(id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_phone.delete_by_id(id, db)
