
from pydantic import BaseModel

class InicioSesionSolicitud(BaseModel):
    usuario: str
    contrasena: str


class UsuarioRespuesta(BaseModel):
    id: int
    usuario: str
    nombre: str
    rol: str


class InicioSesionRespuesta(BaseModel):
    exito: bool
    mensaje: str
    usuario: UsuarioRespuesta