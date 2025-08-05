from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import models, crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books", response_model=list[schemas.BookSchema])
def read_books(db: Session = Depends(get_db)):
    return crud.get_all_books(db)

@app.get("/students", response_model=list[schemas.StudentSchema])
def read_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)

@app.get("/shelfs", response_model=list[schemas.ShelfSchema])
def read_shelfs(db: Session = Depends(get_db)):
    return crud.get_all_shelfs(db)

@app.get("/loans", response_model=list[schemas.LoanSchema])
def read_loans(db: Session = Depends(get_db)):
    return crud.get_all_loans(db)

@app.post("/loans", response_model=schemas.LoanSchema, status_code=201)
def create_loan(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    return crud.create_loan(db, loan)

@app.put("/loans/{loan_id}/return", response_model=schemas.LoanSchema)
def return_loan(loan_id: int, db: Session = Depends(get_db)):
    return crud.return_loan(db, loan_id)
