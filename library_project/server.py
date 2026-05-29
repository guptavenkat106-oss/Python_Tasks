from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session,
    relationship
)

from pydantic import BaseModel

from datetime import datetime, timedelta

# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI()

# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# =========================================================
# DATABASE
# =========================================================

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/library_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# =========================================================
# BOOK TABLE
# =========================================================

class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))

    author = Column(String(255))

    category = Column(String(255))

    price = Column(Float)

    available = Column(Boolean, default=True)

    transactions = relationship(
        "Transaction",
        back_populates="book"
    )

# =========================================================
# USER TABLE
# =========================================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255))

    email = Column(String(255), unique=True)

    membership = Column(String(100))

# =========================================================
# TRANSACTION TABLE
# =========================================================

class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    book_id = Column(
        Integer,
        ForeignKey("books.id")
    )

    issued_to = Column(String(255))

    issued_by = Column(String(255))

    issue_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    due_date = Column(
        DateTime,
        default=lambda:
        datetime.utcnow() + timedelta(days=14)
    )

    return_date = Column(
        DateTime,
        nullable=True
    )

    book = relationship(
        "Book",
        back_populates="transactions"
    )

    fine = relationship(
        "Fine",
        back_populates="transaction",
        uselist=False
    )

# =========================================================
# FINE TABLE
# =========================================================

class Fine(Base):

    __tablename__ = "fines"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(
        Integer,
        ForeignKey("transactions.id")
    )

    amount = Column(Float)

    is_paid = Column(Boolean, default=False)

    transaction = relationship(
        "Transaction",
        back_populates="fine"
    )

# =========================================================
# CREATE TABLES
# =========================================================

Base.metadata.create_all(bind=engine)

# =========================================================
# PYDANTIC SCHEMAS
# =========================================================

class BookCreate(BaseModel):

    title: str
    author: str
    category: str
    price: float

class UserCreate(BaseModel):

    name: str
    email: str
    membership: str

class IssueBook(BaseModel):

    issued_to: str
    issued_by: str

# =========================================================
# DATABASE DEPENDENCY
# =========================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# =========================================================
# HOME
# =========================================================

@app.get("/")
def home():

    return {
        "message": "Library API Running"
    }

# =========================================================
# BOOK APIs
# =========================================================

@app.post("/books")
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):

    new_book = Book(**book.model_dump())

    db.add(new_book)

    db.commit()

    db.refresh(new_book)

    return {
        "message": "Book Added"
    }

@app.get("/books")
def get_books(
    db: Session = Depends(get_db)
):

    return db.query(Book).all()

# =========================================================
# USER APIs
# =========================================================

@app.post("/users")
def add_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(**user.model_dump())

    db.add(new_user)

    db.commit()

    return {
        "message": "User Added"
    }

@app.get("/users")
def get_users(
    db: Session = Depends(get_db)
):

    return db.query(User).all()

# =========================================================
# ISSUE BOOK
# =========================================================

@app.post("/issue-book/{book_id}")
def issue_book(
    book_id: int,
    issue_data: IssueBook,
    db: Session = Depends(get_db)
):

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book Not Found"
        )

    if not book.available:

        raise HTTPException(
            status_code=400,
            detail="Book Already Issued"
        )

    transaction = Transaction(
        book_id=book_id,
        issued_to=issue_data.issued_to,
        issued_by=issue_data.issued_by
    )

    book.available = False

    db.add(transaction)

    db.commit()

    return {
        "message": "Book Issued"
    }

# =========================================================
# RETURN BOOK
# =========================================================

@app.post("/return-book/{book_id}")
def return_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    transaction = db.query(Transaction).filter(
        Transaction.book_id == book_id,
        Transaction.return_date == None
    ).first()

    if not transaction:

        raise HTTPException(
            status_code=404,
            detail="Transaction Not Found"
        )

    now = datetime.utcnow()

    transaction.return_date = now

    book = db.query(Book).filter(
        Book.id == book_id
    ).first()

    book.available = True

    if now > transaction.due_date:

        days = (
            now - transaction.due_date
        ).days

        fine_amount = days * 5

        fine = Fine(
            transaction_id=transaction.id,
            amount=fine_amount
        )

        db.add(fine)

    db.commit()

    return {
        "message": "Book Returned"
    }

# =========================================================
# FINE APIs
# =========================================================

# =========================================================
# ADD FINE
# =========================================================

class FineCreate(BaseModel):

    transaction_id: int
    amount: float

@app.post("/fines")
def add_fine(
    fine_data: FineCreate,
    db: Session = Depends(get_db)
):

    transaction = db.query(Transaction).filter(
        Transaction.id == fine_data.transaction_id
    ).first()

    if not transaction:

        raise HTTPException(
            status_code=404,
            detail="Transaction Not Found"
        )

    fine = Fine(
        transaction_id=fine_data.transaction_id,
        amount=fine_data.amount
    )

    db.add(fine)

    db.commit()

    return {
        "message": "Fine Added Successfully"
    }

# =========================================================
# PAY FINE
# =========================================================

@app.put("/pay-fine/{fine_id}")
def pay_fine(
    fine_id: int,
    db: Session = Depends(get_db)
):

    fine = db.query(Fine).filter(
        Fine.id == fine_id
    ).first()

    if not fine:

        raise HTTPException(
            status_code=404,
            detail="Fine Not Found"
        )

    fine.is_paid = True

    db.commit()

    return {
        "message": "Fine Paid Successfully"
    }

# =========================================================
# GET SINGLE FINE
# =========================================================

@app.get("/fines/{fine_id}")
def get_single_fine(
    fine_id: int,
    db: Session = Depends(get_db)
):

    fine = db.query(Fine).filter(
        Fine.id == fine_id
    ).first()

    if not fine:

        raise HTTPException(
            status_code=404,
            detail="Fine Not Found"
        )

    return fine

@app.get("/fines")
def get_fines(
    db: Session = Depends(get_db)
):

    return db.query(Fine).all()
