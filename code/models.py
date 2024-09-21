from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    JSON,
    String,
    BigInteger,
    DATE,
    Float,
    Computed,
    DateTime,
    Enum,
    ARRAY,
    event,
    TIMESTAMP,
)
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import Base

from config import setting

class User(Base):
    __tablename__ = "user"

    id = Column(Integer,nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, default="")
    gender = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    dob = Column(DATE, nullable=True)
    parent_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)

class LoginLogs(Base):
    __tablename__ = "login_logs"
    id = Column(Integer, primary_key=True, index=True)
    ph = Column(Integer, nullable=True)
    email = Column(String, nullable=True)
    datetime = Column(DateTime, server_default=func.now(), nullable=False)