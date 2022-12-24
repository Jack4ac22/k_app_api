from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum, Float, Date, DateTime
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
    username = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    secret_password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)


class DbPerson(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(Enum(personalized_enums.Genders_person), nullable=False)
    email = Column(String, nullable=False, unique=True)
    birthday = Column(Date, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(),
                        onupdate=func.current_timestamp(), nullable=True)
    # TODO: forign kwy related to user....
    added_by = Column(Integer, nullable=False)
