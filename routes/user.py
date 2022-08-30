# Response sirve para devolver HTTP como returns. Se importa tambn desde starlette el paquetre status
from fastapi import APIRouter, Response
# conn es la variable que me permite conectar con la db ver en config
from config.db import conn
from models.user import atletas
# desde el archivo user de schemas importo la clase User (ver en argumento de funcion post)
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

# ---------OBTENER TODOS LOS ATLETAS DE LA DB


@user.get("/atletas", response_model=list[User])
def get_atletas():
    # retorna una consulta a la db
    return conn.execute(atletas.select()).fetchall()

# ---------AGEGAR ATLETA A LA DB


@user.post("/atletas")
def create_atleta(user: User):
    new_atleta = {"name": user.name, "email": user.email, "date": user.date}
    print(new_atleta)
    # result guarda el ID del alteta guardado
    result = conn.execute(atletas.insert().values(new_atleta))
    # consulta a la db el id (alojado en reult)
    return conn.execute(atletas.select().where(atletas.c.id == result.lastrowid)).first()
    # y devuelve el objeto que ha guardado
# ---------OBTENER ATLETA POR ID                                                                                                                                                                           #esto lo vemos en/docs al crear un atleta


@user.get("/atletas/{id}")
def atleta_por_id(id: str):
    return conn.execute(atletas.select().where(atletas.c.id == id)).first()

# ---------BORRAR ATLETA POR ID


@user.delete("/atletas/{id}")
def delete_atleta_por_id(id: str):
    conn.execute(atletas.delete().where(atletas.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

# ---------ACTUALIZAR ATLETA POR ID


@user.put("/atletas/{id}")
def update_atleta_por_id(id: str, user: User):
    conn.execute(atletas.update().values(
        name=user.name, email=user.email, date=user.date).where(atletas.c.id== id))
    return conn.execute(atletas.select().where(atletas.c.id == id)).first()
