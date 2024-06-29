from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import crud, schemas, utils
from .database import get_db  # Импортируем get_db из файла database.py

router = APIRouter()

@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_phone(db, phone_number=user.phone_number)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Phone number already registered")
    created_user = crud.create_user(db, user)
    utils.send_verification_sms(created_user.phone_number)  # Предполагается, что эта функция реализована в utils.py
    return created_user

@router.post("/verify", response_model=schemas.User)
def verify_user(phone_number: str, code: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_phone(db, phone_number=phone_number)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if utils.verify_sms_code(phone_number, code):
        user.verified = True
        db.commit()
        return user
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid verification code")
