from fastapi import APIRouter, Depends
from db.database import get_db
from schemas import phone_schemas
from sqlalchemy.orm.session import Session
from db import db_phone
from typing import List

router = APIRouter(
    prefix="/phone",
    tags=["phone"]
)

@router.post("",response_model=phone_schemas.PhoneDisplay)
def create_new_phone(request: phone_schemas.PhoneBase, db: Session = Depends(get_db)):
    return db_phone.create_phone(request, db)


@router.get("/all",response_model=List[phone_schemas.PhoneDisplay])
def get_all_phones(db: Session = Depends(get_db)):
    return db_phone.get_all(db)
