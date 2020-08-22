from fastapi import FastAPI
from recursos import customer

app = FastAPI()
app.include_router(customer.router)

@app.get("/")
def home():
    return {"Flosspa":"Api Lab wit FASTAPI"}

@app.get("/dias")
def dias():
    return {"1":"domingo","2": "Lunes","3":"Martes"}

