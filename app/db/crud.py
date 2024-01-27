from sqlalchemy.orm import Session
from app.db import schemas
from app.api.models.user import User


def get_all_users(db: Session, offset: int = 0, limit: int = 10):
    return db.query(User).offset(offset).limit(limit).all()


def get_user_by_email(db, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    new_user = User(email=user.email, username=user.username, password=user.password, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def update_user(db: Session, email: str, user: schemas.UserUpdate):
    db_user = get_user_by_email(db, email)
    if db_user:
        for attr, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, attr, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, email: str):
    db_user = get_user_by_email(db, email)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
