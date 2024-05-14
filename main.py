from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name:str
    lastName:str
    Age:int
    curso:str

app = FastAPI()

# estos son los metodos http mas se usan, o operaciones
# POST: para crear datos.
# GET: para leer datos.
# PUT: para actualizar datos.
# DELETE: para eliminar datos.

@app.get("/")
def hello_world():
    return {"saludo": "Hello Worl" }

@app.post("/crate/user")
def create_user(user:User):
    return {"response": "Usuario creado correctamente", "user":user }




# ejecutar server -uvicorn main:app --reload-