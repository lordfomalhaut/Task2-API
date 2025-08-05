from sqlalchemy import Column, Integer, String, Boolean, SmallInteger, ForeignKey, Date
from app.database import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "Book"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    isbn = Column(String(20), unique=True)
    publication_year = Column(SmallInteger)
    available = Column(Boolean, default=True)
    shelf_id = Column(Integer, ForeignKey("Shelf.shelf_id"))
    category_id = Column(Integer, ForeignKey("Category.category_id"))


class Student(Base):
    __tablename__ = "Student"

    student_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    program = Column(String(100), nullable=False)

class Shelf(Base):
    __tablename__ = "Shelf"

    shelf_id = Column(Integer, primary_key=True, index=True)
    location = Column(String(50), nullable=False)
    topic = Column(String(100), nullable=False)
    material = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)

class Category(Base):
    __tablename__ = "Category"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

class Loan(Base):
    __tablename__ = "Loan"

    loan_id = Column(Integer, primary_key=True, index=True)
    loan_date = Column(Date, nullable=False)
    estimated_return_date = Column(Date, nullable=False)
    actual_return_date = Column(Date, nullable=True)

    student_id = Column(Integer, ForeignKey("Student.student_id"), nullable=False)
    book_id = Column(Integer, ForeignKey("Book.book_id"), nullable=False)

    student = relationship("Student")
    book = relationship("Book") 