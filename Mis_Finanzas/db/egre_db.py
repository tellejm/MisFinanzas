from typing import Dict
from models.egresos import Egresos

database_egresos = Dict[str,Egresos]

database_egresos = {
    1: Egresos(**{
        "Idegresos": 1  ,
        "descripcion":"Arriendo" ,
        "frecuencia":"mensual"  ,
        "importe":330.0   ,
        "fecha_de_vencimiento":"2020-12-01 23:59:59.000000" ,
        "estado":"realizado" ,
        "categoría":"Pagos Recurrentes",
        "fecha_lanzamiento":"2020-11-01 08:59:00.000000" ,
        "fecha_pago":"2020-12-01 00:00:00.000000",
        "observaciones":"Bueno" ,
        "username":"Jhon"
    }),
    2: Egresos(**{
        "Idegresos": 2,
        "descripcion": "Pago Electricidad",
        "frecuencia": "mensual",
        "importe": 75.0,
        "fecha_de_vencimiento": "2020-12-15 23:59:59.000000",
        "estado": "realizado",
        "categoría": "Pagos Recurrentes",
        "fecha_lanzamiento": "2020-11-01 09:00:00.000000",
        "fecha_pago": "2020-12-10 00:00:00.000000",
        "observaciones": "Bueno",
        "username": "Jhon"
    }),
    3: Egresos(**{
        "Idegresos": 3,
        "descripcion": "Pago Acueducto",
        "frecuencia": "mensual",
        "importe": 45.0,
        "fecha_de_vencimiento": "2020-12-10 23:59:59.000000",
        "estado": "realizado",
        "categoría": "Pagos Recurrentes",
        "fecha_lanzamiento": "2020-11-01 09:01:00.000000",
        "fecha_pago": "2020-12-10 00:00:00.000000",
        "observaciones": "Bueno",
        "username": "Jhon"
    })
}


def get_egreso(Idegresos: int):
    if Idegresos in database_egresos.keys():
        return database_egresos[Idegresos]
    else:
        return None

def set_egreso(egreso_in_db: Egresos):
    database_egresos[egreso_in_db.Idegresos] = egreso_in_db
    return egreso_in_db
