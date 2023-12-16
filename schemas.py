from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Schema for creating a new post
class PostCreate(BaseModel):
    title: str
    text: str
    author: str


# Schema for updating an existing post
class PostUpdate(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None
    author: Optional[str] = None


# Schema for reading post data
class Post(BaseModel):
    id: int
    title: str
    text: str
    dateOfCreation: datetime
    author: str

    class Config:
        orm_mode = True
