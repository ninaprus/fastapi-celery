from tasks import fetch_books
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session, joinedload
from database import SessionLocal
from typing import List
import models
import schema


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books")
def read_books(db: Session = Depends(get_db), response_model=List[schema.BookSchema]):
    books = db.query(models.Book).options(
        joinedload(models.Book.author),
        joinedload(models.Book.categories)
    ).all()
    return books

@app.get("/celery")
async def celery_read_books():
    fetch_books.apply_async()
    return {"status": "Ok"}
