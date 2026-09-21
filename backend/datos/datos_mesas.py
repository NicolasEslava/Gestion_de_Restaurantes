from modelos.mesa import Mesa
from datos.conexion import conectar


def obtener_mesas_db():

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_mesa,
            numero,
            estado
        FROM mesas
        ORDER BY numero
    """)

    mesas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return mesas


def buscar_mesa_db(numero):

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_mesa,
            numero,
            estado
        FROM mesas
        WHERE numero = %s
    """, (numero,))

    mesa = cursor.fetchone()

    cursor.close()
    conexion.close()

    return mesa


def crear_mesa_db(numero):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO mesas (numero, estado)
        VALUES (%s, %s)
    """, (numero, "libre"))

    conexion.commit()

    id_mesa = cursor.lastrowid

    cursor.close()
    conexion.close()

    return id_mesa


def actualizar_mesa_db(numero_actual, nuevo_numero):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE mesas
        SET numero = %s
        WHERE numero = %s
    """, (nuevo_numero, numero_actual))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas


def eliminar_mesa_db(numero):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM mesas
        WHERE numero = %s
    """, (numero,))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas


def ocupar_mesa_db(numero):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE mesas
        SET estado = 'ocupada'
        WHERE numero = %s
    """, (numero,))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas


def liberar_mesa_db(numero):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE mesas
        SET estado = 'libre'
        WHERE numero = %s
    """, (numero,))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    return filas_afectadas
