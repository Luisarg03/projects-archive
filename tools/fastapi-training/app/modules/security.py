import os
import hashlib
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .conf import cursor_confs, get_db
from . import crud

# FOR DEVELOPMENT ENV
from dotenv import load_dotenv
load_dotenv()

SALT = os.environ.get("SALT")
ROUNDS = int(os.environ.get("ROUNDS", 1))
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 1))

CursorPage = cursor_confs()
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(stored_password_hash, provided_password, salt, rounds):
    hashed_provided_password = hashlib.pbkdf2_hmac(
        'sha256',
        provided_password.encode('utf-8'),
        salt.encode('utf-8'),
        rounds
    )

    return hashed_provided_password.hex() == stored_password_hash


def authenticate_user(db: Session, username: str, password: str, salt: str, rounds: int):
    user = crud.get_user_api(db, username)
    if not user:
        return False
    if not verify_password(user.password, password, salt, rounds):
        return False
    return user


def create_access_token(data: dict, token_expire_minutes: int, secret_key: str, algorithm: str):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=token_expire_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid username")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password, SALT, ROUNDS)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token = create_access_token(
        data={"sub": user.username},
        token_expire_minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
        secret_key=SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {"access_token": access_token, "token_type": "bearer"}
