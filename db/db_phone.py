from sqlalchemy.orm.session import Session
from schemas import person_schemas, personalized_enums, phone_schemas
from .models import DbPerson, DbPhone
import datetime


def create_phone(request: phone_schemas.PhoneBase, db: Session):

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
