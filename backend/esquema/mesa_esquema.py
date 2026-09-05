from pydantic import BaseModel


class MesaCrear(BaseModel):
    numero: int


class MesaActualizar(BaseModel):
    nuevo_numero: int
