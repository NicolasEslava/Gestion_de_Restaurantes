from typing import Optional, List
from pydantic import BaseModel, Field


class DetallePedidoCrear(BaseModel):
    id_plato: int
    cantidad: int = Field(gt=0)
    observacion: Optional[str] = None


class DetallePedidoRespuesta(BaseModel):
    id_detalle: int
    id_plato: int
    nombre_plato: str
    precio_unitario: float
    cantidad: int
    observacion: Optional[str]
    subtotal: float


class PedidoCrear(BaseModel):
    id_mesa: int


class PedidoRespuesta(BaseModel):
    id_pedido: int
    id_mesa: int
    detalles: List[DetallePedidoRespuesta]
    subtotal: float
    total: float


class DetallePedidoModificar(BaseModel):
    cantidad: Optional[int] = Field(
        default=None,
        gt=0
    )

    observacion: Optional[str] = None
