from sqlalchemy.orm.session import Session
from schemas import person_schemas, user_schemas, personalized_enums
from .models import DbUser, DbPerson
from utilities import hash_manager
import datetime


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
    all_posts = db.query(DbPerson).all()
    return all_posts
