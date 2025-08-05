This part of the assessment corresponds to Task 2 and was developed based on the database model created in Task 1.

I decided to build a simple API using the data model from Task 1, utilizing FastAPI and SQLAlchemy. The API includes endpoints to retrieve books, students, shelves, and loans, as well as to create and return a loan.


to run the project: uvicorn app.main:app --reload


## API Structure
The API is organized into several files for better modularity and maintainability:

models.py: Contains the SQLAlchemy ORM models that define the structure of the database tables.

schemas.py: Defines the Pydantic models used for data validation and serialization in the API requests and responses.

database.py: Handles the database connection and session management.

crud.py: Contains the functions for interacting with the database.

main.py: entry point of the application. uses the functions from crud.py to implement the API endpoints.

