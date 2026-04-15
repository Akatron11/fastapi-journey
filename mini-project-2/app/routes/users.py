from fastapi import APIRouter, HTTPException
from database.connection import Database
from models.users import User, UserSignIn

user_router = APIRouter()
user_database = Database(User)

@user_router.post("/signup")
async def sign_new_user(data: User):
    # E-posta adresiyle daha önce kayıt olunmuş mu kontrol et
    user_exist = await User.find_one(User.email == data.email)
    if user_exist:
        raise HTTPException(status_code=409, detail="User with this email already exists")
    
    await user_database.save(data)
    return {"message": "User registered successfully"}

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn):
    # Kullanıcıyı veritabanında ara
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(status_code=404, detail="User does not exist")
    
    # Şifre kontrolü (Şu an düz metin olarak kontrol ediyoruz)
    if user_exist.password == user.password:
        return {"message": "User signed in successfully"}
    
    raise HTTPException(status_code=401, detail="Invalid password")