from fastapi import FastAPI
from .enrollment import enrollment_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Course Enrollment System. Go to /home for UI."}

app.include_router(enrollment_router)