
from fastapi import FastAPI

from db.ing_db import database_ingresos, set_ingresos
from db.user_db import database_users, set_user
from models.ingresos import Ingresos
from models.user import User
api = FastAPI()

@api.post("/users")
def saveUser(user: User):
    set_user(user)
    return database_users


@api.post("/ingresos")

def saveIngresos(ingresos: Ingresos):
    set_ingresos(ingresos)
    return database_ingresos

