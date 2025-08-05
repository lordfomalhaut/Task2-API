from sqlalchemy.orm import Session
from app.models import Book, Student, Shelf, Loan
from app.schemas import LoanCreate
from fastapi import HTTPException
from datetime import date

def get_all_books(db: Session):
    return db.query(Book).all()

def get_all_students(db: Session):
    return db.query(Student).all()

def get_all_shelfs(db: Session):
    return db.query(Shelf).all()

def get_all_loans(db: Session):
    loans = db.query(Loan).join(Student).join(Book).all()
    return loans

def create_loan(db: Session, loan: LoanCreate):
    book = db.query(Book).filter(Book.book_id == loan.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="El libro no existe")
    
    if not book.available:
        raise HTTPException(status_code=400, detail="El libro no esta disponible para prestamo")
    
    existing_loan = db.query(Loan).filter(
        Loan.book_id == loan.book_id,
        Loan.actual_return_date == None
    ).first()

    if existing_loan:
        raise HTTPException(status_code=400, detail="Este libro ya fue prestado y no ha sido devuelto")

    new_loan = Loan(**loan.model_dump())
    db.add(new_loan)
    book.available = False
    db.commit()
    db.refresh(new_loan)
    return new_loan

def return_loan(db: Session, loan_id: int):
    loan = db.query(Loan).filter(Loan.loan_id == loan_id).first()

    if not loan:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    
    if loan.actual_return_date is not None:
        raise HTTPException(status_code=400, detail="El préstamo ya fue devuelto")
    
    loan.actual_return_date = date.today()

    book = db.query(Book).filter(Book.book_id == loan.book_id).first()
    if book:
        book.available = True
    
    db.commit()
    db.refresh(loan)
    return loan