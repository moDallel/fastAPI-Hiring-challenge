from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app.db.database import engine


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    age = Column(Integer)
    password = Column(String)


Base.metadata.create_all(engine)
