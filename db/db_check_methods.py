from sqlalchemy.orm.session import Session
from .models import DbPerson, DbPhone, DbComment, DbTask, DbUser
from fastapi import HTTPException, status

############################
### User's check methods ###
############################


def check_person_id(person_id: int, db: Session):
    person = db.query(DbPerson).filter(DbPerson.id == person_id)
    if not person.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding person was found with ID: {person_id}, please verify the ID and try again."
        )
    return person
