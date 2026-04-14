from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# Aynı klasördeki modelleri almak için nokta (.) kullanımı zorunludur
from .models import Student, EnrollmentRecord

# 1. Router Tanımlama (Hocanın istediği isim: enrollment_router)
enrollment_router = APIRouter()

# 2. Jinja2 Ayarı (Klasör yolu ana dizine göre ayarlandı)
templates = Jinja2Templates(directory="mini-project-1/templates")

# 3. Geçici Veritabanı (HTML şablonundaki değişkenlerle birebir uyumlu)
students_db = [
    {
        "id": 1, 
        "student_name": "Suleyman Faruk Sahal", 
        "course": "Software Engineering", 
        "gpa": 3.8,
        "courses": [{"course_name": "Backend Development", "semester": "Spring 2024"}]
    }
]

# --- HTML SAYFA ROTALARI (Requirement 3) ---

# enrollment.py içindeki home fonksiyonu
@enrollment_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,  # Bu satır en üstte ve bu isimle olmalı
        name="home.html", 
        context={"enrollments": students_db}
    )

# enrollment.py içindeki detay fonksiyonu
@enrollment_router.get("/enrollment/{id}", response_class=HTMLResponse)
async def get_item_page(request: Request, id: int):
    selected_student = next((s for s in students_db if s["id"] == id), None)
    
    if selected_student:
        return templates.TemplateResponse(
            request=request,  # Yine en üstte ve açıkça belirterek
            name="enrollment.html", 
            context={"enrollment": selected_student}
        )
    raise HTTPException(status_code=404, detail="Student not found")

# --- API (JSON) ROTALARI (Requirement 1) ---

@enrollment_router.get("/students/")
async def get_all_students():
    return students_db

@enrollment_router.post("/students/")
async def create_student(student: Student):
    students_db.append(student.model_dump())
    return student

@enrollment_router.put("/students/{student_id}")
async def update_student(student_id: int, updated_student: Student):
    for i, s in enumerate(students_db):
        if s["id"] == student_id:
            students_db[i] = updated_student.model_dump()
            return {"message": "Updated successfully", "data": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")

@enrollment_router.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for i, s in enumerate(students_db):
        if s["id"] == student_id:
            del students_db[i]
            return {"message": f"Student {student_id} deleted"}
    raise HTTPException(status_code=404, detail="Student not found")