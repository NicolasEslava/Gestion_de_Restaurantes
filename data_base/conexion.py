import os
import mysql.connector


def obtener_conexion():
    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "")
    database = os.getenv("MYSQL_DATABASE", "gestion_restaurante")
    port = int(os.getenv("MYSQL_PORT", "3306"))

    try:
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            autocommit=True
        )
    except mysql.connector.Error as e:
        print(f"No se pudo conectar a MySQL Workbench: {e}")
        return None