from datetime import date, datetime
from re import compile
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, constr
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from typing import Optional, Literal
import re
from db import get_db


class GetUser(BaseModel):
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    name: str


class UserCreate(BaseModel):
    name: str
    gender: Optional[str] = None
    age: Optional[int] = None
    dob: Optional[date] = None
    parent_name: Optional[str] = None
    email: EmailStr
    password: str
    phone_number: str

class login(BaseModel):
    email: EmailStr
    password: str