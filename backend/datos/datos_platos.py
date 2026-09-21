from modelos.plato import Plato
from datos.conexion import conectar


def eliminar_plato_db(id_plato):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM productos
        WHERE id_producto = %s
    """, (id_plato,))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas


def obtener_productos_db():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_producto,
            nombre_producto,
            descripcion,
            precio,
            categoria,
            estado
        FROM productos
    """)

    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return productos


def obtener_platos_db():
    productos = obtener_productos_db()

    platos = []

    for producto in productos:
        plato = Plato(
            id_plato=producto["id_producto"],
            nombre=producto["nombre_producto"],
            precio=producto["precio"],
            categoria=producto["categoria"],
            disponible=producto["estado"] == "disponible"
        )

        platos.append(plato)

    return platos


def buscar_plato_db(id_plato):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_producto,
            nombre_producto,
            descripcion,
            precio,
            categoria,
            estado
        FROM productos
        WHERE id_producto = %s
    """, (id_plato,))

    producto = cursor.fetchone()

    cursor.close()
    conexion.close()

    return producto


def crear_plato_db(nombre, precio, categoria):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO productos
        (nombre_producto, precio, categoria, estado)
        VALUES (%s, %s, %s, %s)
    """, (nombre, precio, categoria, "disponible"))

    conexion.commit()

    id_plato = cursor.lastrowid

    cursor.close()
    conexion.close()

    return id_plato


def actualizar_plato_db(id_plato, nombre, precio, categoria, disponible):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE productos
        SET nombre_producto = %s,
            precio = %s,
            categoria = %s,
            estado = %s
        WHERE id_producto = %s
    """, (
        nombre,
        precio,
        categoria,
        "disponible" if disponible else "no disponible",
        id_plato
    ))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas
