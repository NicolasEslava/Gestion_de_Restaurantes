from typing import Optional, List
from pydantic import BaseModel


class DetallePrefacturaRespuesta(BaseModel):
    id_detalle: int
    id_plato: int
    nombre_plato: str
    precio_unitario: float
    cantidad: int
    observacion: Optional[str] = None
    subtotal: float


class PrefacturaRespuesta(BaseModel):
    id_prefactura: int
    id_pedido: int
    id_mesa: int
    detalles: List[DetallePrefacturaRespuesta]
    subtotal: float
    total: float
