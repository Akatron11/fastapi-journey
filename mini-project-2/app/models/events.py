from beanie import Document
from pydantic import BaseModel
from typing import List, Optional

# Veritabanına kaydedilecek asıl döküman
class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Settings:
        name = "events" # MongoDB'deki tablo (koleksiyon) adı

# Güncelleme işlemleri için kullanılacak yardımcı model
class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None