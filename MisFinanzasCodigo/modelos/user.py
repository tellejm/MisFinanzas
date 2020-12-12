from pydantic import BaseModel

class User(BaseModel):
    name:str
    passw:str
    email:str
    username:str

        
class UserInit(BaseModel):
    usuario: str
    Apellido: str
    Contraseña: str
    Correo: str
    Ciudad: str
    Edad: int
    Extracto: str
    Ocupación: str
    Estado_civil: str
    Numero_de_hijos: int
