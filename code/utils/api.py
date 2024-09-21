import re
from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def secure_pwd(raw_password):
    hashed = pwd_context.hash(raw_password)

    return hashed


def verify_pwd(plain, hash):
    return pwd_context.verify(plain, hash)


def validate_password(payload):
    if len(payload.password) < 8:
        raise HTTPException(
            status_code=400, detail="Password must be at least 8 characters long"
        )

    if not re.search(r"[a-z]", payload.password):
        raise HTTPException(
            status_code=400, detail="Password must include lowercase letters"
        )

    if not re.search(r"[A-Z]", payload.password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one uppercase letter",
        )

    if not re.search(r"\d", payload.password):
        raise HTTPException(
            status_code=400, detail="Password must contain at least one numeric digit"
        )

    if not re.search(r"[@#$!%*?&]", payload.password):
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least one special character (e.g., !, @, #, $, %)",
        )
