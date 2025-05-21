from pydantic import BaseModel
from datetime import date

class EmployeeBase(BaseModel):
    name: str
    department: str
    health_score: float
    attendance_percentage: float
    date_joined: date

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
