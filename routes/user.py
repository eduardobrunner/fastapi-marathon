from fastapi import APIRouter, Response #Response sirve para devolver HTTP como returns. Se importa tambn desde starlette el paquetre status
from config.db import conn #conn es la variable que me permite conectar con la db ver en config
from models.user import atletas
from schemas.user import User #desde el archivo user de schemas importo la clase User (ver en argumento de funcion post)
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get("/atletas")
def get_atletas():
    return conn.execute(atletas.select()).fetchall() #retorna una consulta a la db

@user.post("/atletas")
def create_atleta(user: User): 
    new_atleta = {"name": user.name, "email":user.email, "date":user.date}
    print (new_atleta)
    result = conn.execute(atletas.insert().values(new_atleta)) #result guarda el ID del alteta guardado
    return conn.execute(atletas.select().where(atletas.c.id == result.lastrowid)).first()#consulta a la db el id (alojado en reult)
                                                                                         #y devuelve el objeto que ha guardado
                                                                                         #esto lo vemos en/docs al crear un atleta
@user.get("/atletas/{id}")
def atleta_por_id(id: str):
    return conn.execute(atletas.select().where(atletas.c.id == id)).first() 

@user.delete("/atletas/{id}")
def delete_atleta_por_id(id: str):
    conn.execute(atletas.delete().where(atletas.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
                                                                                    

