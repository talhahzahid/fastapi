from fastapi import APIRouter, exceptions, Request, exception_handlers, HTTPException

router = APIRouter()

employees = {1: "Ali", 2: "Ahmed", 3: "Sara"}


@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    employee = employees.get(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"name": employee}


# Custom Exception and Global Exception


class EmployeeNotFoundError(Exception):
    pass


# global exception
