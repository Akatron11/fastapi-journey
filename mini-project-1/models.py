from pydantic import BaseModel, Field, model_validator
from typing import List, Optional

class EnrollmentRecord(BaseModel):
    course_name: str = Field(..., min_length=3) 
    semester: str 

class Student(BaseModel):
    id: int = Field(..., gt=0) 
    student_name: str  
    course: str 
    gpa: float = Field(..., ge=0, le=4.0) 
    courses: List[EnrollmentRecord] = []

    @model_validator(mode='after')
    def validate_names(self):
        if not self.student_name.strip():
            raise ValueError("Student name cannot be empty")
        return self