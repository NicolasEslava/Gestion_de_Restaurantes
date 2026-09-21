from fastapi import HTTPException

from modelos.pedido import Pedido, DetallePedido
from datos.datos_pedidos import (pedidos, contador_pedido, contador_detalle)
from servicios.mesa_servicio import MesaServicio
from servicios.platos_servicios import Platoservicio


def buscar_pedido_por_mesa(id_mesa: int):

    for pedido in pedidos:
        if pedido.id_mesa == id_mesa:
            return pedido

    return None


def buscar_pedido(id_pedido: int):

    for pedido in pedidos:
        if pedido.id_pedido == id_pedido:
            return pedido

    return None


def buscar_detalle(pedido: Pedido, id_detalle: int):

    for detalle in pedido.detalles:
        if detalle.id_detalle == id_detalle:
            return detalle

    return None


def buscar_plato(id_plato: int):

    servicio_platos = Platoservicio()

    return servicio_platos.buscar_plato(id_plato)


def crear_pedido(id_mesa: int):

    global contador_pedido

    servicio_mesas = MesaServicio()

    mesa = servicio_mesas.buscar_mesa(id_mesa)

    if mesa is None:
        raise HTTPException(
            status_code=404,
            detail="La mesa no existe."
        )


def agregar_detalle(
    id_pedido: int,
    id_plato: int,
    cantidad: int,
    observacion=None
):

    global contador_detalle

    pedido = buscar_pedido(id_pedido)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    if cantidad <= 0:
        raise HTTPException(
            status_code=400,
            detail="La cantidad debe ser mayor que cero."
        )

    plato = buscar_plato(id_plato)

    if not plato:
        raise HTTPException(
            status_code=404,
            detail="El plato no existe."
        )

    if not plato.disponible:
        raise HTTPException(
            status_code=400,
            detail="El plato no está disponible."
        )

    # Si el plato ya está dentro del pedido,
    # aumentamos la cantidad en lugar de duplicarlo.
    for detalle in pedido.detalles:

        if detalle.id_plato == id_plato:

            detalle.cantidad += cantidad

            if observacion is not None:
                detalle.observacion = observacion

            return detalle

    nuevo_detalle = DetallePedido(
        id_detalle=contador_detalle,
        id_plato=id_plato,
        cantidad=cantidad,
        observacion=observacion
    )

    pedido.detalles.append(nuevo_detalle)

    contador_detalle += 1

    return nuevo_detalle


def modificar_detalle(
    id_pedido: int,
    id_detalle: int,
    cantidad: int = None,
    observacion=None
):

    pedido = buscar_pedido(id_pedido)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    detalle = buscar_detalle(
        pedido,
        id_detalle
    )

    if not detalle:
        raise HTTPException(
            status_code=404,
            detail="El detalle no existe."
        )

    if cantidad is not None:

        if cantidad <= 0:
            raise HTTPException(
                status_code=400,
                detail="La cantidad debe ser mayor que cero."
            )

        detalle.cantidad = cantidad

    if observacion is not None:
        detalle.observacion = observacion

    return detalle


def eliminar_detalle(
    id_pedido: int,
    id_detalle: int
):

    pedido = buscar_pedido(id_pedido)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    detalle = buscar_detalle(
        pedido,
        id_detalle
    )

    if not detalle:
        raise HTTPException(
            status_code=404,
            detail="El detalle no existe."
        )

    pedido.detalles.remove(detalle)

    return {
        "mensaje": "Producto eliminado del pedido."
    }


def obtener_pedido(id_pedido: int):

    pedido = buscar_pedido(id_pedido)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    return pedido


def calcular_pedido(id_pedido: int):

    pedido = buscar_pedido(id_pedido)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    detalles = []

    subtotal_pedido = 0

    for detalle in pedido.detalles:

        plato = buscar_plato(
            detalle.id_plato
        )

        if not plato:
            continue

        subtotal = (
            plato.precio *
            detalle.cantidad
        )

        subtotal_pedido += subtotal

        detalles.append({
            "id_detalle": detalle.id_detalle,
            "id_plato": plato.id_plato,
            "nombre_plato": plato.nombre,
            "precio_unitario": plato.precio,
            "cantidad": detalle.cantidad,
            "observacion": detalle.observacion,
            "subtotal": subtotal
        })

    return {
        "id_pedido": pedido.id_pedido,
        "id_mesa": pedido.id_mesa,
        "detalles": detalles,
        "subtotal": subtotal_pedido,
        "total": subtotal_pedido
    }
