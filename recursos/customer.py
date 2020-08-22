from fastapi import APIRouter
from mysqlconnector import conecta
from pydantic import BaseModel

router = APIRouter()

@router.get("/customers")
def clientes(): 
    db = conecta()
    if db:
        with db.cursor() as cursor:
            result = cursor.execute("Select * from customers") 
            resultado = cursor.fetchall()
            #cols = [str(x[0]) for x in cursor.description]
            json_resultado = []
            for row in resultado:
                json = dict()           
                json["customerNumber"] = str(row[0])
                json["customerName"] = row[1]
                json["contactLastName"] = row[2]
                json["contactFirstName"] = row[3]
                json["phone"] = row[4]
                json["city"] = row[5]
                json["creditLimit"] = row[6]
                json_resultado.append(json)

            print(str(json_resultado))
            return json_resultado	

@router.get("/customers/{x}")
def clientes(x:int,param2 = None): 
    """
    Esta funcion devuelve un cliente puntual
    """
    db = conecta()
    if db:
        with db.cursor() as cursor:
            result = cursor.execute(f"Select * from customers where customerNumber={x}") 
            resultado = cursor.fetchall()
            #cols = [str(x[0]) for x in cursor.description]
            json_resultado = []
            for row in resultado:
                json = dict()           
                json["customerNumber"] = str(row[0])
                json["customerName"] = row[1]
                json["contactLastName"] = row[2]
                json["contactFirstName"] = row[3]
                json["phone"] = row[4]
                json["city"] = row[5]
                json["creditLimit"] = row[6]
                json_resultado.append(json)

            print(str(json_resultado))
            return json_resultado	
