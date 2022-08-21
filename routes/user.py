from fastapi import APIRouter
from config.db import conn #conn es la variable que me permite conectar con la db ver en config
from models.user import atletas
from schemas.user import User #desde el archivo user de schemas importo la clase User (ver en argumento de funcion post)

user = APIRouter()

@user.get("/atletas")
def get_atletas():
    return conn.execute(atletas.select()).fetchall() #retorna una consulta a la db

@user.post("/atletas")
def create_atleta(user: User): 
    print (user)
    return "probando post"
