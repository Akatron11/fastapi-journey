from fastapi import FastAPI
import uvicorn
from database.connection import initialize_database
from routes.events import event_router
from routes.users import user_router

app = FastAPI()

# 1. Uygulama Başlarken Veritabanını Başlat (Requirement 5)
@app.on_event("startup")
async def start_db():
    await initialize_database()

# 2. Rotaları (Routes) Kaydet (Requirement 3 & 4)
# Prefix kullanarak URL'leri grupluyoruz
app.include_router(event_router, prefix="/event", tags=["Events"])
app.include_router(user_router, prefix="/user", tags=["Users"])

@app.get("/")
async def home():
    return {"message": "Welcome to the Event Planner API with MongoDB!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)