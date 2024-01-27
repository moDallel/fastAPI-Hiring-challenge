from sqlalchemy.orm import Session
from . import schemas
from app.api.models.user import User

# def get_all_users(db):
#     return db
# def get_user_by_email(db, email: str):
#     return db.query(User).filter(User.email == email).first()
#
#
def create_user(db: Session, user: schemas.UserCreate):
    new_user = User(email=user.email, username=user.username, password=user.password, firstName=user.firstName, lastName=user.lastName, tel=user.tel)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
#
#
# def update_user(db: Session, email: str, user: schemas.UserUpdate):
#     db_user = get_user_by_email(db, email)
#     if db_user:
#         for attr, value in user.dict(exclude_unset=True).items():
#             setattr(db_user, attr, value)
#         db.commit()
#         db.refresh(db_user)
#     return db_user
#
#
# def delete_user(db: Session, email: str):
#     db_user = get_user_by_email(db, email)
#     if db_user:
#         db.delete(db_user)
#         db.commit()
#     return db_user
