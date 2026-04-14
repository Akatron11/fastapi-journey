from fastapi import FastAPI, HTTPException
import asyncio
from models import Student, Enrollment

app = FastAPI()

# Geçici Veritabanı
students_db = [
    {
        "id": 1, 
        "name": "Suleyman Sahal", 
        "age": 22, 
        "email": "fsahal@uni.edu",
        "enrollments": [{"course_name": "FastAPI 101", "semester": "Spring"}]
    }
]

@app.get("/students/")
async def get_all_students():
    return students_db

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    # Simüle edilmiş gecikme (Requirement 4)
    await asyncio.sleep(1) 
    for s in students_db:
        if s["id"] == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")

