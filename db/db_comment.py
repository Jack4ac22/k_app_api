from sqlalchemy.orm.session import Session
from schemas import comment_schemas
from .models import DbComment
from db import db_comment, db_check_methods
from fastapi import HTTPException, status


def check_comment_id(id: int, db: Session):
    comment = db.query(DbComment).filter(DbComment.id == id)
    if not comment.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding comment was found with ID: {id}, please verify the ID and try again."
        )
    return comment


def create_comment(request: comment_schemas.CommentBase, db: Session):
    db_check_methods.check_person_id(request.person_id, db)
    new_comment = DbComment(
        person_id=request.person_id,
        title=request.title,
        content=request.content
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db: Session):
    all_comments = db.query(DbComment).all()
    return all_comments


def get_comment_by_id(id: int, db: Session):
    comment = check_comment_id(id, db)
    return comment.first()


def get_personal_comments(person_id: int, db: Session):
    db_check_methods.check_person_id(person_id, db)
    comments = db.query(DbComment).filter(
        DbComment.person_id == person_id).all()
    if not comments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No corresponding comments were found for the person of ID: {person_id}, please verify and try again."
        )
    return comments


def update(id: int, request: comment_schemas.CommentBase, db: Session):
    targeted_comment = check_comment_id(id, db)
    targeted_comment.update(request.dict())
    db.commit()
    return targeted_comment.first()
