import mysql.connector


def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Restaurante2026!",
        database="gestion_restaurante"
    )

    return conexion
