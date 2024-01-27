from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from ...db import schemas, crud

router = APIRouter()


# @router.get("/users/")
# def get_all_users():
#     return crud.get_all_users(db=db)
@router.post("/create/")
async def create_user(user: schemas.UserCreate, db : Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


# @router.get("/users/{email}", response_model=schemas.User)
# def get_user_by_email(email: str, db: Session = Depends(get_db)):
#     user = crud.get_user_by_email(db, email=email)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user
#
#
# @router.put("/users/{email}", response_model=schemas.User)
# def update_user(email: str, user: schemas.UserUpdate, db: Session = Depends(get_db)):
#     updated_user = crud.update_user(db, email=email, user=user)
#     if updated_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return updated_user
#
#
# @router.delete("/users/{email}", response_model=schemas.User)
# def delete_user(email: str, db: Session = Depends(get_db)):
#     deleted_user = crud.delete_user(db, email=email)
#     if deleted_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return deleted_user
