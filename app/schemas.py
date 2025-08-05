from pydantic import BaseModel
from datetime import date


class BaseModelOrmMode(BaseModel):
    class Config:
        from_attributes = True

class CategorySchema(BaseModelOrmMode):
    category_id: int
    name: str

class BookSchema(BaseModelOrmMode):
    book_id: int
    title: str
    author: str
    isbn: str
    publication_year: int
    available: bool
    shelf_id: int
    category_id: int

class StudentSchema(BaseModelOrmMode):
    student_id: int
    name: str
    email: str
    program: str

class ShelfSchema(BaseModelOrmMode):
    shelf_id: int
    location: str
    topic: str
    material: str
    capacity: int

class LoanBase(BaseModelOrmMode):
    student_id: int
    book_id: int
    loan_date: date
    estimated_return_date: date
    actual_return_date: date | None = None

class LoanCreate(LoanBase):
    pass

class LoanSchema(LoanBase):
    loan_id: int
    student: StudentSchema
    book: BookSchema