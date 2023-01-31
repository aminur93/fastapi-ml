from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    email: str
    age: int
    country: str

