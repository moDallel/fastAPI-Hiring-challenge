from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app.db.database import engine


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    firstName = Column(String)
    lastName = Column(String)
    tel = Column(Integer, unique=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String)

    # def __repr__(self):
    #     return f"<User(id={self.id}, email={self.email}, username={self.username})>"


Base.metadata.create_all(engine)