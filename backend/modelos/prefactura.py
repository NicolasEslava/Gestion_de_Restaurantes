class DetallePrefactura:
    def _init_(self, id_detalle: int, id_plato: int, nombre_plato: str, precio_unitario: float, cantidad: int, observacion=None, subtotal: float = 0):
        self.id_detalle = id_detalle
        self.id_plato = id_plato
        self.nombre_plato = nombre_plato
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.observacion = observacion
        self.subtotal = subtotal


class Prefactura:
    def _init_(self, id_prefactura: int, id_pedido: int, id_mesa: int, detalles=None, subtotal: float = 0, total: float = 0):
        self.id_prefactura = id_prefactura
        self.id_pedido = id_pedido
        self.id_mesa = id_mesa
        self.detalles = detalles or []
        self.subtotal = subtotal
        self.total = total
