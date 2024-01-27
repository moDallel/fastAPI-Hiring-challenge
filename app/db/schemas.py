from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    age: int


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    email: str = None
    username: str = None
    password: str = None
    age: int = None


class User(UserBase):
    id: int
