from fastapi import HTTPException
from modelos.prefactura import (Prefactura, DetallePrefactura)
from datos.datos_prefactura import (prefacturas, contador_prefactura)
from datos.datos_pedidos import pedidos
from datos.datos_platos import platos


def buscar_pedido(id_pedido: int):

    for pedido in pedidos:

        if pedido.id_pedido == id_pedido:
            return pedido

    return None


def buscar_plato(id_plato: int):

    for plato in platos:

        if plato.id_plato == id_plato:
            return plato

    return None


def buscar_prefactura(id_prefactura: int):

    for prefactura in prefacturas:

        if prefactura.id_prefactura == id_prefactura:
            return prefactura

    return None


def buscar_prefactura_por_pedido(id_pedido: int):

    for prefactura in prefacturas:

        if prefactura.id_pedido == id_pedido:
            return prefactura

    return None


def calcular_detalle(precio_unitario: float, cantidad: int):

    return precio_unitario * cantidad


def crear_prefactura(id_pedido: int):

    global contador_prefactura

    # Buscar el pedido
    pedido = buscar_pedido(id_pedido)

    if pedido is None:

        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    # Verificar si ya existe una prefactura
    prefactura_existente = buscar_prefactura_por_pedido(id_pedido)

    if prefactura_existente is not None:

        raise HTTPException(status_code=400, detail="El pedido ya tiene una prefactura."
                            )

    detalles_prefactura = []

    subtotal_general = 0

    # Recorrer los detalles del pedido
    for detalle in pedido.detalles:

        plato = buscar_plato(detalle.id_plato)

        if plato is None:

            raise HTTPException(
                status_code=404,
                detail=(
                    f"El plato con ID "
                    f"{detalle.id_plato} "
                    f"no existe."
                )
            )

        subtotal_detalle = calcular_detalle(plato.precio, detalle.cantidad)

        detalle_prefactura = DetallePrefactura(id_detalle=detalle.id_detalle, id_plato=plato.id_plato, nombre_plato=plato.nombre,
                                               precio_unitario=plato.precio, cantidad=detalle.cantidad, observacion=detalle.observacion, subtotal=subtotal_detalle)

        detalles_prefactura.append(detalle_prefactura)

        subtotal_general += subtotal_detalle

    # Crear la prefactura
    nueva_prefactura = Prefactura(id_prefactura=contador_prefactura, id_pedido=pedido.id_pedido,
                                  id_mesa=pedido.id_mesa, detalles=detalles_prefactura, subtotal=subtotal_general, total=subtotal_general)

    prefacturas.append(nueva_prefactura)

    contador_prefactura += 1

    return nueva_prefactura


def obtener_prefactura(id_prefactura: int):

    prefactura = buscar_prefactura(id_prefactura)

    if prefactura is None:

        raise HTTPException(status_code=404, detail="La prefactura no existe.")

    return prefactura


def obtener_prefactura_por_pedido(id_pedido: int):

    prefactura = buscar_prefactura_por_pedido(id_pedido)

    if prefactura is None:

        raise HTTPException(
            status_code=404, detail="El pedido no tiene prefactura.")

    return prefactura
