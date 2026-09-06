from typing import List, Optional


class DetallePedido:
    def __init__(
        self,
        id_detalle: int,
        id_plato: int,
        cantidad: int,
        observacion: Optional[str] = None
    ):
        self.id_detalle = id_detalle
        self.id_plato = id_plato
        self.cantidad = cantidad
        self.observacion = observacion


class Pedido:
    def __init__(
        self,
        id_pedido: int,
        id_mesa: int,
        detalles: Optional[List[DetallePedido]] = None
    ):
        self.id_pedido = id_pedido
        self.id_mesa = id_mesa
        self.detalles = detalles or []
