from datos.conexion import conectar


def crear_pedido_db(id_mesa, estado, observaciones=None):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO pedidos
        (id_mesa, estado, observaciones)
        VALUES (%s, %s, %s)
    """, (
        id_mesa,
        estado,
        observaciones
    ))

    conexion.commit()

    id_pedido = cursor.lastrowid

    cursor.close()
    conexion.close()

    return id_pedido


def buscar_pedido_db(id_pedido):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_pedido,
            id_mesa,
            fecha,
            estado,
            observaciones
        FROM pedidos
        WHERE id_pedido = %s
    """, (id_pedido,))

    pedido = cursor.fetchone()

    cursor.close()
    conexion.close()

    return pedido


def buscar_pedido_por_mesa_db(id_mesa):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_pedido,
            id_mesa,
            fecha,
            estado,
            observaciones
        FROM pedidos
        WHERE id_mesa = %s
        ORDER BY id_pedido DESC
        LIMIT 1
    """, (id_mesa,))

    pedido = cursor.fetchone()

    cursor.close()
    conexion.close()

    return pedido


def obtener_detalles_db(id_pedido):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_detalle_pedido,
            id_pedido,
            id_producto,
            cantidad,
            precio_unitario,
            observaciones
        FROM detalle_pedido
        WHERE id_pedido = %s
    """, (id_pedido,))

    detalles = cursor.fetchall()

    cursor.close()
    conexion.close()

    return detalles


def crear_detalle_db(
    id_pedido,
    id_producto,
    cantidad,
    precio_unitario,
    observaciones=None
):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO detalle_pedido
        (
            id_pedido,
            id_producto,
            cantidad,
            precio_unitario,
            observaciones
        )
        VALUES (%s, %s, %s, %s, %s)
    """, (
        id_pedido,
        id_producto,
        cantidad,
        precio_unitario,
        observaciones
    ))

    conexion.commit()

    id_detalle = cursor.lastrowid

    cursor.close()
    conexion.close()

    return id_detalle


def buscar_detalle_db(id_detalle):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_detalle_pedido,
            id_pedido,
            id_producto,
            cantidad,
            precio_unitario,
            observaciones
        FROM detalle_pedido
        WHERE id_detalle_pedido = %s
    """, (id_detalle,))

    detalle = cursor.fetchone()

    cursor.close()
    conexion.close()

    return detalle


def actualizar_detalle_db(
    id_detalle,
    cantidad,
    observaciones
):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE detalle_pedido
        SET cantidad = %s,
            observaciones = %s
        WHERE id_detalle_pedido = %s
    """, (
        cantidad,
        observaciones,
        id_detalle
    ))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas


def eliminar_detalle_db(id_detalle):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM detalle_pedido
        WHERE id_detalle_pedido = %s
    """, (id_detalle,))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas


def buscar_pedido_pendiente_por_mesa_db(id_mesa):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_pedido,
            id_mesa,
            fecha,
            estado,
            observaciones
        FROM pedidos
        WHERE id_mesa = %s
          AND estado = 'pendiente'
        ORDER BY id_pedido DESC
        LIMIT 1
    """, (id_mesa,))

    pedido = cursor.fetchone()

    cursor.close()
    conexion.close()

    return pedido


def actualizar_estado_pedido_db(id_pedido, estado):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE pedidos
        SET estado = %s
        WHERE id_pedido = %s
    """, (
        estado,
        id_pedido
    ))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas
