from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session
from typing import List
from blog import schemas, models
from blog.database import get_db
from blog import hashing

def get_user(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    return user

def create_user(user: schemas.User, db: Session):
    hashed_password = hashing.Hash().encrypt_password(user.password)
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        return None
    new_user = models.User(name=user.name, email=user.email, password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user