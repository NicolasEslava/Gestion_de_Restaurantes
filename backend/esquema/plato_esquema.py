from pydantic import BaseModel


class PlatoCrear (BaseModel):
    nombre: str
    precio: float
    categoria: str


class PlatoActualizar (BaseModel):
    nombre: str | None = None
    precio: float | None = None
    categoria: str | None = None
    disponible: bool | None = None
