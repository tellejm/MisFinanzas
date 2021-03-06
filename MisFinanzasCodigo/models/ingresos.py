from pydantic import BaseModel
from datetime import datetime

class Ingresos(BaseModel):
    Idigresos:int
    username:str
    descripcion:str
    frecuencia:str 
    importe:float
    fecha_de_vencimiento:datetime
    estado:str
    categoría:str
    fecha_lanzamiento:datetime
    fecha_pago:datetime
    observaciones:str