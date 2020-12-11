from db.user_db import UserInDB
from typing import Dict
from db.user_db import update_user, get_user, database_users
from models.user_models import UserIn, UserOut



import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.get("/",)
def inicio():
    return "Pagina de inicio"

@api.get("/users/all/", response_model=Dict[str, UserInDB])
async def get_users():
    return database_users

@api.post("/users/user/data/create/{username}")      
async def update_user(username: str, user_in_db: UserInDB):
    
    database_users[username] = user_in_db
    # return database_users[username]
    return user_in_db

@api.post("/users/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado correctamente"}

@api.get("/users/user/data/{username}")
async def get_balance(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.put("/users/user/data/update/{username}")      
async def update_user(username: str, user_in_db: UserInDB):
    
    try:
        database_users[username] = user_in_db
        return database_users[username]
    
    except:
        raise HTTPException(status_code=404, detail="No existe el usuario")
        
    
    return user_in_db

@api.delete("/users/user/delete/{username}")
async def delete_user(username: str):
    
    try:
        del database_users[username]
        return database_users
    
    except:
        raise HTTPException(status_code=404, detail="Usuario no existe")
