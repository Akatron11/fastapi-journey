from beanie import init_beanie, Document
from motor.motor_asyncio import AsyncIOMotorClient
# 3. satırı bu şekilde değiştir:
from pydantic_settings import BaseSettings
from typing import List, Any, Optional
# Modelleri aynı klasör seviyesinden çağırmak için başına nokta koyabilirsin
from models.events import Event
from models.users import User

# 1. Ayarlar Sınıfı (.env dosyasını okur)
class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    class Config:
        env_file = "mini-project-2/.env"

# 2. Veritabanını Başlatma Fonksiyonu
async def initialize_database():
    settings = Settings()
    # 1. Bağlantıyı kur
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    
    # 2. Veritabanı ismini buraya açıkça yazıyoruz (Garanti çözüm)
    # Bu satır, veritabanı yoksa bile MongoDB'ye 'planner' ismini kullanmasını söyler.
    database = client.planner 
    
    # 3. Beanie'yi başlat
    await init_beanie(
        database=database,
        document_models=[Event, User]
    )

# 3. Hocanın İstediği Genel Database Sınıfı
class Database:
    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: Any):
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        return await self.model.find_all().to_list()

    async def update(self, id: Any, body: Any):
        doc = await self.get(id)
        if not doc:
            return False
        # Gönderilen veriyi sözlüğe çevirip güncelleme yapıyoruz
        update_query = {"$set": body.model_dump(exclude_unset=True)}
        await doc.update(update_query)
        return doc

    async def delete(self, id: Any):
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True