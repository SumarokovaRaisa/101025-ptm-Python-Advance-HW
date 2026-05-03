from pydantic import BaseModel, Field
from typing import List, Optional


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)


class QuestionResponse(BaseModel):
    id: int
    text: str


class MessageResponse(BaseModel):
    message: str


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True # Позволяет Pydantic работать с моделями SQLAlchemy


class QuestionBase(BaseModel):
    text: str
    category_id: int

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    category: Optional[CategoryResponse] = None


    class Config:
        from_attributes = True





