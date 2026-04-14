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

@app.post("/students/")
async def create_student(student: Student):
    students_db.append(student.model_dump())
    return student

@app.put("/students/{student_id}")
async def update_student(student_id: int, updated_student: Student):
    for i, s in enumerate(students_db):
        if s["id"] == student_id:
            students_db[i] = updated_student.model_dump()
            return {"message": "Updated successfully", "data": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for i, s in enumerate(students_db):
        if s["id"] == student_id:
            del students_db[i]
            return {"message": f"Student {student_id} deleted"}
    raise HTTPException(status_code=404, detail="Student not found")