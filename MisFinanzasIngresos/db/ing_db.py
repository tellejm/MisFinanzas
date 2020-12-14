from typing import Dict
from models.ingresos import Ingresos



database_ingresos = Dict[str,Ingresos]

database_ingresos = {

    1: Ingresos(**{
        "Idingresos": 1  ,
        "descripcion":"nomina" ,
        "frecuencia":"mensual"  ,
        "valor":990.0  ,
        "estado":"realizado" ,
        "categoría":"Ingresos Fijos",
        "fecha_lanzamiento":"2020-12-14 10:00:00.000000" ,
        "observaciones":"Ingresos generados por trabajo en compañía" ,
        "username":"xxxx"
    }),
    2: Ingresos(**{
        "Idingresos": 2  ,
        "descripcion":"horas extras" ,
        "frecuencia":"semanal"  ,
        "valor":340.0   ,
        "estado":"realizado" ,
        "categoría":"Ingresos variables",
        "fecha_lanzamiento":"2020-12-14 10:00:00.000000" ,
        "observaciones":"Ingresos generados por trabajo semanal nocturno" ,
        "username":"xxxx"
    }),
}


def get_ingresos(Idingresos: int):
    if Idingresos in database_ingresos.keys():
        return database_ingresos[Idingresos]
    else:
        return None

def set_ingresos(ingreso_in_db: Ingresos):
    database_ingresos[ingreso_in_db.Idingresos] = ingreso_in_db
    return ingreso_in_db
