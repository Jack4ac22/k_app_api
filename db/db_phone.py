from sqlalchemy.orm.session import Session
from schemas import person_schemas, personalized_enums, phone_schemas
from .models import DbPerson, DbPhone
import datetime
from db import db_person
from fastapi import HTTPException, status


def check_id(id: int, db: Session):
    phone = db.query(DbPhone).filter(DbPhone.id == id)
    if not phone.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding Phone was found with ID: {id}, please verify the ID and try again."
        )
    return phone


def check_number(nb: str, db: Session):
    phones = db.query(DbPhone).filter(DbPhone.phone.ilike(f'%{nb}%')).all()
    if not phones:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding Phones were found with input: {nb}, please verify the the number and try again."
        )
    return phones


def check_number_usage(nb: str, db: Session):
    phone = db.query(DbPhone).filter(DbPhone.phone == nb).first()
    if phone:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"The phone number: {nb} is used by someone else in your database, please verify."
        )
    return phone


def create_phone(request: phone_schemas.PhoneBase, db: Session):
    db_person.check_id(request.person_id, db)
    # new_phone = DbPhone(**request.dict())
    new_phone = DbPhone(
        person_id=request.person_id,
        phone=request.phone,
        description=request.description,
    )
    db.add(new_phone)
    db.commit()
    db.refresh(new_phone)
    return new_phone


def get_all(db: Session):
    phones = db.query(DbPhone).all()
    return phones


def get_by_id(id: int, db: Session):
    phone = check_id(id, db)
    return phone


def get_by_number(nb: int, db: Session):
    phones = check_number(nb, db)
    return phones


def update(id: int, request: phone_schemas.PhoneBase, db: Session):
    targeted_phone = db.query(DbPhone).filter(DbPhone.id == id)
    if not targeted_phone.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No corresponding phone was found with ID: {id}, please verify the ID and try again.")
    db_person.check_id(request.person_id, db)
    updated_number = request.__dict__['phone']
    original_number = targeted_phone.first().__dict__['phone']
    if updated_number != original_number:
        check_number_usage(updated_number, db)
    targeted_phone.update(request.dict())
    db.commit()
    return targeted_phone.first()


def delete_by_id(id: int, db: Session):
    targeted_phone = check_id(id, db)
    deleted_phone = targeted_phone.first()
    print(deleted_phone)
    targeted_phone.delete()
    db.commit()
    return deleted_phone
