from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum, Float, Date, DateTime,TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
import enum
from schemas import personalized_enums
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, index=True, unique=True)
    password = Column(String, nullable=False)
    secret_password = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)


class DbPerson(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(Enum(personalized_enums.Genders_person), nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    birthday = Column(Date, nullable=True, server_default="1900-01-31")
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(),
                        onupdate=func.current_timestamp(), nullable=True)
    added_by = Column(Integer, ForeignKey("user.id"))
    user = relationship("DbUser")
    phones = relationship("DbPhone", back_populates='person')



class DbPhone(Base):
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("person.id"))
    phone = Column(String, nullable=False, unique=True, index=True)
    description = Column(String, nullable=False,
                         unique=True, server_default="personal")
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(),
                        onupdate=func.current_timestamp(), nullable=True)
    person = relationship("DbPerson", back_populates='phones')


class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    person_id = Column(Integer, ForeignKey("person.id"))
    title = Column(String, nullable=True, unique=False)
    content = Column(TEXT, nullable=True,
                     unique=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(),
                        onupdate=func.current_timestamp(), nullable=True)
    person = relationship("DbPerson")
