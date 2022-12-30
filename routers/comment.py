from fastapi import APIRouter, Depends, status
from db.database import get_db
from schemas import comment_schemas
from sqlalchemy.orm.session import Session
from db import db_comment
from typing import List
from utilities import jwt_manager

router = APIRouter(
    prefix="/comment",
    tags=["comment"]
)


@router.post("", response_model=comment_schemas.CommentDisplay, status_code=status.HTTP_201_CREATED)
def create_new_comment(request: comment_schemas.CommentBase, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_comment.create_comment(request, db)


@router.get("/all", response_model=List[comment_schemas.CommentDisplay])
def get_all_comments(db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_comment.get_all(db)


@router.get("/com{id}", response_model=comment_schemas.CommentDisplay)
def get_single_comment_by_id(id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_comment.get_comment_by_id(id, db)


@router.get("per{person_id}", response_model=List[comment_schemas.CommentDisplaySimple])
def get_all_comments_for_person(person_id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_comment.get_personal_comments(person_id, db)


@router.put("{id}", response_model=comment_schemas.CommentDisplay)
def update_comment(id: int, request: comment_schemas.CommentBase, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_comment.update(id, request, db)


@router.delete("{id}", response_model=comment_schemas.CommentDisplaySimple)
def delete_comment(id: int, db: Session = Depends(get_db), user_id: int = Depends(jwt_manager.decode_token)):
    return db_comment.delete(id, db)
