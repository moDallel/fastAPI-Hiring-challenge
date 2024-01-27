from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    firstName: str
    lastName: str
    tel: int


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

