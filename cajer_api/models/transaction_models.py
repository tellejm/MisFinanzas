from pydantic import BaseModel
from datetime import datetime
class TransactionIn(BaseModel):
    username: str
    password:str
    nombre:str
    apellido:str
    correo:str
    ciudad:str
    edad:str
    estrato:str
    ocupacion:str
    estado_civil:str
    numero_hijos:str

class TransactionOut(BaseModel):
    username: str
    password:str
    nombre:str
    apellido:str
    correo:str
    ciudad:str
    edad:str
    estrato:str
    ocupacion:str
    estado_civil:str
    numero_hijos:str
