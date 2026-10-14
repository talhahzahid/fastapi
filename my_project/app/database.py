from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.exc import SQLAlchemyError

from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from fastapi import APIRouter, Depends, HTTPException, status

DATABASE_URL = "sqlite:///./test.db"

router = APIRouter()

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class EmployeeTable(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    designation = Column(String)
    address = Column(String)
    isEmployee = Column(Boolean)


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


@router.post(
    "/create-employee",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = EmployeeTable(**employee.model_dump())
    try:
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unable to create employee",
        )


@router.get(
    "/employees", response_model=list[EmployeeResponse], status_code=status.HTTP_200_OK
)
def get_employee(db: Session = Depends(get_db)):
    employees = db.query(EmployeeTable).all()
    return employees


@router.get("/employee/{employee_id}")
def get_employee_id(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(EmployeeTable).filter(EmployeeTable.id == employee_id).first()

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.put("/employee/{employee_id}")
def update_employee(
    employee_id: int, employee_data: EmployeeUpdate, db: Session = Depends(get_db)
):
    employee = db.query(EmployeeTable).filter(EmployeeTable.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    employee.name = employee_data.name
    employee.age = employee_data.age
    employee.designation = employee_data.designation

    db.commit()
    db.refresh(employee)

    return employee


@router.delete("/employee/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(EmployeeTable).filter(EmployeeTable.id == employee_id).first()

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()

    return {"message": "Employee deleted successfully"}
