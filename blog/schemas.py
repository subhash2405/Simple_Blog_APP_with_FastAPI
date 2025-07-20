from pydantic import BaseModel, Field
import re
from typing import List, Optional

class BaseBlog(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1, max_length=5000)
    # class Config:
    #     orm_mode = True

class blog(BaseBlog):
    class Config:
        orm_mode = True

class User(BaseModel):
    name : str = Field(..., min_length=1, max_length=50)
    email: str = Field(..., max_length=100)
    password: str = Field(..., min_length=6, max_length=100)


class showUser(BaseModel):
    name : str
    email: str
    blogs : List[blog] = []
    class Config:
        orm_mode = True


class ShowBlog(BaseModel):

    title: str
    content: str
    owner: Optional[showUser]

    class Config:
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None