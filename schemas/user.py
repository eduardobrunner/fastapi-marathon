from typing import Optional
from pydantic import BaseModel  #pydantic permite añadir tipos de datos

class User(BaseModel):
    id: Optional[str]
    name: str
    email: str
    date: str
    