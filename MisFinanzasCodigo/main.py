
from fastapi import FastAPI

from db.ingre_db import database_ingresos, set_ingresos
from db.egre_db import database_egresos, set_egresos
from db.user_db import database_users, set_user
from models.ingresos import Ingresos
from models.user import User
from models.egresos import Egresos
api = FastAPI()

@api.post("/users")
def saveUser(user: User):
    set_user(user)
    return database_users


@api.post("/ingresos")

def saveIngresos(ingresos: Ingresos):
    set_ingresos(ingresos)
    return database_ingresos

@api.post("/egresos")
def saveEgresos(egresos: Egresos):
    set_egresos(egresos)
    return database_egresos
