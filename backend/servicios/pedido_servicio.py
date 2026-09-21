from fastapi import HTTPException

from modelos.pedido import Pedido, DetallePedido
from datos.datos_pedidos import (crear_pedido_db, buscar_pedido_db, buscar_pedido_por_mesa_db, buscar_pedido_pendiente_por_mesa_db,
                                 obtener_detalles_db, crear_detalle_db, buscar_detalle_db, actualizar_detalle_db, eliminar_detalle_db, actualizar_estado_pedido_db)
from servicios.mesa_servicio import MesaServicio
from servicios.platos_servicios import Platoservicio


def convertir_pedido(pedido_db):
    """
    Convierte el registro de MySQL a un objeto Pedido.
    """

    detalles_db = obtener_detalles_db(
        pedido_db["id_pedido"]
    )

    detalles = []

    for detalle in detalles_db:

        nuevo_detalle = DetallePedido(
            id_detalle=detalle["id_detalle_pedido"],
            id_plato=detalle["id_producto"],
            cantidad=detalle["cantidad"],
            observacion=detalle["observaciones"],
            precio_unitario=detalle["precio_unitario"]
        )

        detalles.append(nuevo_detalle)

    return Pedido(
        id_pedido=pedido_db["id_pedido"],
        id_mesa=pedido_db["id_mesa"],
        detalles=detalles
    )


def buscar_pedido_por_mesa(id_mesa: int):

    pedido_db = buscar_pedido_por_mesa_db(id_mesa)

    if pedido_db is None:
        return None

    return convertir_pedido(pedido_db)


def buscar_pedido(id_pedido: int):

    pedido_db = buscar_pedido_db(id_pedido)

    if pedido_db is None:
        return None

    return convertir_pedido(pedido_db)


def buscar_detalle(pedido: Pedido, id_detalle: int):

    detalle_db = buscar_detalle_db(id_detalle)

    if detalle_db is None:
        return None

    # Verificamos que el detalle pertenezca al pedido.
    if detalle_db["id_pedido"] != pedido.id_pedido:
        return None

    return DetallePedido(
        id_detalle=detalle_db["id_detalle_pedido"],
        id_plato=detalle_db["id_producto"],
        cantidad=detalle_db["cantidad"],
        observacion=detalle_db["observaciones"],
        precio_unitario=detalle_db["precio_unitario"]
    )


def buscar_plato(id_plato: int):

    servicio_platos = Platoservicio()

    return servicio_platos.buscar_plato(id_plato)


def crear_pedido(id_mesa: int):
    servicio_mesas = MesaServicio()

    mesa = servicio_mesas.buscar_mesa(id_mesa)

    if mesa is None:
        raise HTTPException(
            status_code=404,
            detail="La mesa no existe."
        )

    pedido_pendiente = buscar_pedido_pendiente_por_mesa_db(
        id_mesa
    )

    if pedido_pendiente is not None:
        raise HTTPException(
            status_code=409,
            detail=(
                f"La mesa ya tiene una cuenta pendiente. "
                f"Pedido: {pedido_pendiente['id_pedido']}"
            )
        )

    id_pedido = crear_pedido_db(
        id_mesa,
        "pendiente"
    )

    return buscar_pedido(id_pedido)


def agregar_detalle(
    id_pedido: int,
    id_plato: int,
    cantidad: int,
    observacion=None
):

    pedido = buscar_pedido(id_pedido)

    if pedido is None:
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

    if plato is None:
        raise HTTPException(
            status_code=404,
            detail="El plato no existe."
        )

    if not plato.disponible:
        raise HTTPException(
            status_code=400,
            detail="El plato no está disponible."
        )

    # Revisamos si el plato ya existe en el pedido.
    for detalle in pedido.detalles:

        if detalle.id_plato == id_plato:

            nueva_cantidad = (
                detalle.cantidad + cantidad
            )

            nueva_observacion = observacion

            if observacion is None:
                nueva_observacion = detalle.observacion

            actualizar_detalle_db(
                detalle.id_detalle,
                nueva_cantidad,
                nueva_observacion
            )

            return buscar_detalle(
                pedido,
                detalle.id_detalle
            )

    # Si el plato no existe, creamos un nuevo detalle.
    id_detalle = crear_detalle_db(
        id_pedido=id_pedido,
        id_producto=id_plato,
        cantidad=cantidad,
        precio_unitario=plato.precio,
        observaciones=observacion
    )

    return buscar_detalle(
        pedido,
        id_detalle
    )


def modificar_detalle(
    id_pedido: int,
    id_detalle: int,
    cantidad: int = None,
    observacion=None
):

    pedido = buscar_pedido(id_pedido)

    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    detalle = buscar_detalle(
        pedido,
        id_detalle
    )

    if detalle is None:
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

        nueva_cantidad = cantidad

    else:
        nueva_cantidad = detalle.cantidad

    nueva_observacion = observacion

    if observacion is None:
        nueva_observacion = detalle.observacion

    actualizar_detalle_db(
        id_detalle,
        nueva_cantidad,
        nueva_observacion
    )

    return buscar_detalle(
        pedido,
        id_detalle
    )


def eliminar_detalle(
    id_pedido: int,
    id_detalle: int
):

    pedido = buscar_pedido(id_pedido)

    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    detalle = buscar_detalle(
        pedido,
        id_detalle
    )

    if detalle is None:
        raise HTTPException(
            status_code=404,
            detail="El detalle no existe."
        )

    filas_afectadas = eliminar_detalle_db(
        id_detalle
    )

    if filas_afectadas == 0:
        raise HTTPException(
            status_code=404,
            detail="El detalle no existe."
        )

    return {
        "mensaje": "Producto eliminado del pedido."
    }


def obtener_pedido(id_pedido: int):

    pedido = buscar_pedido(id_pedido)

    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    return pedido


def calcular_pedido(id_pedido: int):

    pedido = buscar_pedido(id_pedido)

    if pedido is None:
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

        if plato is None:
            continue

        subtotal = (
            detalle.precio_unitario *
            detalle.cantidad
        )

        subtotal_pedido += subtotal

        detalles.append({
            "id_detalle": detalle.id_detalle,
            "id_plato": plato.id_plato,
            "nombre_plato": plato.nombre,
            "precio_unitario": detalle.precio_unitario,
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


def cerrar_pedido(id_pedido: int):
    pedido_db = buscar_pedido_db(id_pedido)

    if pedido_db is None:
        raise HTTPException(
            status_code=404,
            detail="El pedido no existe."
        )

    if pedido_db["estado"] == "pagado":
        raise HTTPException(
            status_code=400,
            detail="La cuenta ya está pagada."
        )

    actualizar_estado_pedido_db(
        id_pedido,
        "pagado"
    )

    servicio_mesas = MesaServicio()

    mesa = servicio_mesas.buscar_mesa(
        pedido_db["id_mesa"]
    )

    if mesa is not None:
        servicio_mesas.liberar_mesa(
            mesa.numero
        )

    return {
        "mensaje": "Cuenta cerrada correctamente.",
        "id_pedido": id_pedido,
        "id_mesa": pedido_db["id_mesa"],
        "estado": "pagado",
        "mesa": "libre"
    }
