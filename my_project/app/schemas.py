from pydantic import BaseModel, Field, ConfigDict


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=18, le=100)
    designation: str = Field(min_length=2, max_length=100)
    address: str = Field(min_length=3, max_length=255)
    isEmployee: bool = True


class EmployeeUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=18, le=100)
    designation: str = Field(min_length=2, max_length=100)
    address: str = Field(min_length=3, max_length=255)
    isEmployee: bool = True


class EmployeeResponse(EmployeeCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
