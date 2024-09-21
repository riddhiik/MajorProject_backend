from sqlalchemy.orm import Session
from sqlalchemy.sql import func
import re
from utils.api import secure_pwd
from models import User
from fastapi import HTTPException, status


def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    return user 


def get_user_by_phone(db: Session, phone_number: str):
    phone = re.compile(r"^\d{8,}$")

    if phone.match(phone_number):
        return db.query(User).filter(User.phone_number== phone_number).first()
    else:
        return None


def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(func.lower(User.email) == email.lower()).first()
    
    return user
