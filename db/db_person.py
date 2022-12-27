from .models import DbUser, DbPerson
from fastapi import HTTPException, Response, status
from schemas import person_schemas, user_schemas, personalized_enums
from sqlalchemy.orm.session import Session
from utilities import hash_manager
import datetime
from pydantic import EmailStr


def check_email_used(email: str, db: Session):
    result_query = db.query(DbPerson).filter(DbPerson.email == email).first()
    if result_query:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"The email: {email} is used by someone else in your database, please verify."
        )


def check_id(id: int, db: Session):
    result_query = db.query(DbPerson).filter(DbPerson.id == id).first()
    if not result_query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding person was found with ID: {id}, please verify the ID and try again."
        )


def create_person(request: person_schemas.PersonBase, db: Session):

    new_person = DbPerson(
        first_name=request.first_name,
        last_name=request.last_name,
        gender=request.gender,
        email=request.email,
        birthday=request.birthday,
        added_by=request.added_by,
        created_at=datetime.datetime.now()
    )
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person


def get_all(db: Session):
    all_people = db.query(DbPerson).all()
    if not all_people:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No people in your database."
        )
    return all_people


def get_by_id(id: int, db: Session):
    targeted_person = db.query(DbPerson).filter(DbPerson.id == id).first()
    check_id(id, db)
    return targeted_person


def get_by_email(email: EmailStr, db: Session):
    targeted_person = db.query(DbPerson).filter(
        DbPerson.email == email).first()
    if not targeted_person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding person was found with ID: {id}, please verify the ID and try again."
        )
    return targeted_person


def update(id: int, request: person_schemas.PersonBase, db: Session):
    targeted_person = db.query(DbPerson).filter(DbPerson.id == id)
    if not targeted_person.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding person was found with ID: {id}, please verify the ID and try again."
        )
    updated_email = request.__dict__['email']
    original_email = targeted_person.first().__dict__['email']
    if updated_email != original_email:
        checking_results = db.query(DbPerson).filter(
            DbPerson.email == updated_email).first()
        if checking_results:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"The email: {updated_email} is used by someone else in your database, please verify."
            )
    print(updated_email)
    print(original_email)
    targeted_person.update(request.dict())
    db.commit()
    return targeted_person.first()


def delete_by_id(id: int, db: Session):
    check_id(id, db)
    targeted_person = db.query(DbPerson).filter(DbPerson.id == id)
    deleted_data = targeted_person.first()
    targeted_person.delete()
    db.commit()
    return deleted_data
