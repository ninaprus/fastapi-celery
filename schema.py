from pydantic import BaseModel
from typing import List

class AuthorBase(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True


class BookBase(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class BookSchema(BookBase):
    author: AuthorBase
    categories: List[CategoryBase]

    class Config:
        from_attributes = True
