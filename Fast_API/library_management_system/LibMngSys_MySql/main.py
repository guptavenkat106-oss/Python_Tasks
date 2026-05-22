# ======================================================================================
# FASTAPI LIBRARY MANAGEMENT SYSTEM
# ======================================================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
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
    relationship,
    sessionmaker,
    Session
)

from datetime import datetime, timedelta

# ======================================================================================
# FASTAPI APP
# ======================================================================================

app = FastAPI()

# ======================================================================================
# MYSQL CONNECTION
# ======================================================================================

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/library_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ======================================================================================
# BOOK TABLE
# ======================================================================================

class Book_DB(Base):

    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    genre = Column(String(255))

    author_name = Column(String(255))

    price = Column(Float)

    available = Column(Boolean, default=True)

    transactions = relationship(
        "Transaction_DB",
        back_populates="book"
    )

# ======================================================================================
# USER TABLE
# ======================================================================================

class User_DB(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    membership_type = Column(
        String(50),
        default="Standard"
    )

# ======================================================================================
# TRANSACTION TABLE
# ======================================================================================

class Transaction_DB(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    book_id = Column(
        Integer,
        ForeignKey("book.id")
    )

    issued_to = Column(String(255))

    issued_by = Column(String(255))

    issue_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    due_date = Column(
        DateTime,
        default=lambda: datetime.utcnow() + timedelta(days=14)
    )

    return_date = Column(
        DateTime,
        nullable=True
    )

    book = relationship(
        "Book_DB",
        back_populates="transactions"
    )

    fine = relationship(
        "Fine_DB",
        back_populates="transaction",
        uselist=False
    )

# ======================================================================================
# FINES TABLE
# ======================================================================================

class Fine_DB(Base):

    __tablename__ = "fines"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(
        Integer,
        ForeignKey("transactions.id")
    )

    amount = Column(Float)

    is_paid = Column(Boolean, default=False)

    transaction = relationship(
        "Transaction_DB",
        back_populates="fine"
    )

# ======================================================================================
# CREATE TABLES
# ======================================================================================

Base.metadata.create_all(bind=engine)

# ======================================================================================
# PYDANTIC SCHEMAS
# ======================================================================================

class BookCreate(BaseModel):

    title: str

    genre: str

    author_name: str

    price: float


class UserCreate(BaseModel):

    name: str

    email: str

    membership_type: str = "Standard"


class IssueBook(BaseModel):

    issued_to: str

    issued_by: str


class FinePayment(BaseModel):

    is_paid: bool

# ======================================================================================
# DATABASE DEPENDENCY
# ======================================================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ======================================================================================
# BOOK APIs
# ======================================================================================

@app.post("/books")
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):

    new_book = Book_DB(**book.model_dump())

    db.add(new_book)

    db.commit()

    db.refresh(new_book)

    return {
        "message": "Book added successfully",
        "data": new_book
    }

@app.get("/books")
def get_books(db: Session = Depends(get_db)):

    return db.query(Book_DB).all()

# ======================================================================================
# USER APIs
# ======================================================================================

@app.post("/users")
def add_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User_DB(**user.model_dump())

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User added successfully",
        "data": new_user
    }

@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    return db.query(User_DB).all()

# ======================================================================================
# ISSUE BOOK API
# ======================================================================================

@app.post("/issue-book/{book_id}")
def issue_book(
    book_id: int,
    issue_data: IssueBook,
    db: Session = Depends(get_db)
):

    book = db.query(Book_DB).filter(
        Book_DB.id == book_id
    ).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    if not book.available:
        raise HTTPException(
            status_code=400,
            detail="Book already issued"
        )

    transaction = Transaction_DB(
        book_id=book_id,
        issued_to=issue_data.issued_to,
        issued_by=issue_data.issued_by
    )

    book.available = False

    db.add(transaction)

    db.commit()

    return {
        "message": "Book issued successfully"
    }

# ======================================================================================
# RETURN BOOK API
# ======================================================================================

@app.post("/return-book/{book_id}")
def return_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    transaction = db.query(Transaction_DB).filter(
        Transaction_DB.book_id == book_id,
        Transaction_DB.return_date == None
    ).first()

    if not transaction:
        raise HTTPException(
            status_code=404,
            detail="No active transaction found"
        )

    now = datetime.utcnow()

    transaction.return_date = now

    book = db.query(Book_DB).filter(
        Book_DB.id == book_id
    ).first()

    book.available = True

    if now > transaction.due_date:

        days = (now - transaction.due_date).days

        if days > 0:

            fine_amount = days * 2.5

            fine = Fine_DB(
                transaction_id=transaction.id,
                amount=fine_amount
            )

            db.add(fine)

    db.commit()

    return {
        "message": "Book returned successfully"
    }

# ======================================================================================
# FINES APIs
# ======================================================================================

@app.get("/fines")
def get_fines(db: Session = Depends(get_db)):

    return db.query(Fine_DB).all()

@app.put("/fines/{fine_id}")
def pay_fine(
    fine_id: int,
    payment: FinePayment,
    db: Session = Depends(get_db)
):

    fine = db.query(Fine_DB).filter(
        Fine_DB.id == fine_id
    ).first()

    if not fine:
        raise HTTPException(
            status_code=404,
            detail="Fine not found"
        )

    fine.is_paid = payment.is_paid

    db.commit()

    return {
        "message": "Fine payment updated"
    }