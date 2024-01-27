from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from ...db import schemas, crud
from app.utils.useful_functions import *


router = APIRouter()


@router.get("/users/", response_model=list[schemas.User])
async def get_all_users(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: Session = Depends(get_db)):
    return crud.get_all_users(db, offset=skip, limit=limit)


@router.get("/users/{email}", response_model=schemas.User)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/create_user/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # check input
    if already_exit_username(user.username, db):
        raise HTTPException(status_code=400, detail="Username already exist")
    if already_exit_email(user.email, db):
        raise HTTPException(status_code=400, detail="email already exist")
    if not valid_email(user.email):
        raise HTTPException(status_code=400, detail="email not valid")
    if len(user.password) <= 8:
        raise HTTPException(status_code=400, detail="password too short")

    return crud.create_user(db=db, user=user)


@router.put("/update_user/{email}", response_model=schemas.User)
def update_user(email: str, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    if user.email:
        if already_exit_email(user.email, db):
            raise HTTPException(status_code=400, detail="email already exist")
        if not valid_email(user.email):
            raise HTTPException(status_code=400, detail="email not valid")
    if user.username:
        if already_exit_username(user.username, db):
            raise HTTPException(status_code=400, detail="Username already exist")
    if user.password:
        if len(user.password) <= 8:
            raise HTTPException(status_code=400, detail="password too short")
    updated_user = crud.update_user(db, email=email, user=user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@router.delete("/delete_user/{email}", response_model=schemas.User)
def delete_user(email: str, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, email=email)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user
