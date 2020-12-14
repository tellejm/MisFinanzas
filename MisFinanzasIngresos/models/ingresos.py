from pydantic import BaseModel
from datetime import datetime

class Ingresos(BaseModel):
    Idingresos:int
    username:str
    descripcion:str
    frecuencia:str 
    valor:float
    estado:str
    categoría:str
    fecha_lanzamiento:datetime
    observaciones:str