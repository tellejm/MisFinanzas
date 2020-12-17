from fastapi import APIRouter, HTTPException

from db.egre_db import database_egresos, set_egreso
from models.egresos import Egresos

router = APIRouter()

@router.post("/egresos")
def saveEgresos(egresos: Egresos):
    set_egreso(egresos)
    return database_egresos

@router.get('/egresos')
def get_egresos():
    return database_egresos
