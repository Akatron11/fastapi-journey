from pydantic import BaseModel, Field, model_validator
from typing import List, Optional

class Enrollment(BaseModel):
    course_name: str = Field(..., min_length=3) 
    semester: str 

class Student(BaseModel):
    id: int = Field(..., gt=0) 
    name: str
    age: int = Field(20, ge=18)
    email: Optional[str] = "not-provided@school.edu"
    enrollments: List[Enrollment] = [] 

    @model_validator(mode='after')
    def check_name_not_empty(self):
        if not self.name.strip():
            raise ValueError("Name cannot be empty")
        return self