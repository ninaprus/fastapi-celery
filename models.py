
from sqlalchemy import String, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

book_category_table = Table(
    'book_category', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True)
)

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    books = relationship("Book", back_populates="author")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    books = relationship("Book", secondary=book_category_table, back_populates="categories")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")
    categories = relationship("Category", secondary=book_category_table, back_populates="books")
