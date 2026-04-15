from beanie import Document
from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Veritabanına kaydedilecek kullanıcı dökümanı
class User(Document):
    email: EmailStr
    password: str
    # Kullanıcının oluşturduğu etkinliklerin ID listesi
    events: Optional[List[str]] = []

    class Settings:
        name = "users"

# Giriş yaparken (Sign In) kullanılacak yardımcı model
class UserSignIn(BaseModel):
    email: EmailStr
    password: str