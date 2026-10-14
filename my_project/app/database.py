from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import APIRouter, Depends

DATABASE_URL = "sqlite:///./test.db"

router = APIRouter()

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)


# Create database tables
Base.metadata.create_all(bind=engine)


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API endpoint
@router.get("/check")
def home(db: Session = Depends(get_db)):
    return {"message": "DB connected fine"}
