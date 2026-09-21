from fastapi import HTTPException

from modelos.prefactura import Prefactura, DetallePrefactura
from servicios.pedido_servicio import buscar_pedido
from servicios.platos_servicios import Platoservicio


def buscar_plato(id_plato: int):
    servicio_platos = Platoservicio()
    return servicio_platos.buscar_plato(id_plato)


def calcular_detalle(precio_unitario: float, cantidad: int):
    return precio_unitario * cantidad


def crear_prefactura(id_pedido: int):
    pedido = buscar_pedido(id_pedido)

    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    detalles_prefactura = []
    subtotal_general = 0

    for detalle in pedido.detalles:

        plato = buscar_plato(detalle.id_plato)

        if plato is None:
            raise HTTPException(
                status_code=404,
                detail=(
                    f"El plato con ID {detalle.id_plato} "
                    f"no existe."
                )
            )

        subtotal_detalle = calcular_detalle(
            detalle.precio_unitario,
            detalle.cantidad
        )

        detalle_prefactura = DetallePrefactura(
            id_detalle=detalle.id_detalle,
            id_plato=plato.id_plato,
            nombre_plato=plato.nombre,
            precio_unitario=detalle.precio_unitario,
            cantidad=detalle.cantidad,
            observacion=detalle.observacion,
            subtotal=subtotal_detalle
        )

        detalles_prefactura.append(
            detalle_prefactura
        )

        subtotal_general += subtotal_detalle

    return Prefactura(
        id_prefactura=pedido.id_pedido,
        id_pedido=pedido.id_pedido,
        id_mesa=pedido.id_mesa,
        detalles=detalles_prefactura,
        subtotal=subtotal_general,
        total=subtotal_general
    )


def obtener_prefactura(id_prefactura: int):
    return crear_prefactura(id_prefactura)


def obtener_prefactura_por_pedido(id_pedido: int):
    return crear_prefactura(id_pedido)
