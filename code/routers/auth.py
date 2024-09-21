from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.orm import Session

from models import LoginLogs, User
from utils.auth import get_user_by_email, get_user_by_phone
from utils.api import validate_password, verify_pwd
from schemas import UserCreate, login
from passlib.context import CryptContext
from db import get_db


route = APIRouter(prefix="/auth", tags=["Authentication"])


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

@route.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter((User.email == user.email) | (User.phone_number == user.phone_number)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email or phone number already registered")
    
    # Create new user
    hashed_password = hash_password(user.password)
    db_user = User(
    name=user.name,
    gender=user.gender,
    age=user.age,
    dob=user.dob,
    parent_name=user.parent_name,
    email=user.email,
    password=hashed_password,  # Make sure the password is hashed before saving
    phone_number=user.phone_number
)

    db.add(db_user)
    db.commit()
    db.refresh(db_user) 
        
    return db_user


@route.post("/login")
def login_user(payload: login ,db: Session = Depends(get_db)):
    # Fetch the user from the database
    user = db.query(User).filter(User.email == payload.email).first()
    
    # Check if user exists
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Verify the password
    if not verify_password(payload.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return JSONResponse(
        status_code=200,
        content={
            "status_code": 200,
            "message": "User logged in successfully"
        }
    )
