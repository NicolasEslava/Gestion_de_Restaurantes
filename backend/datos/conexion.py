import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def obtener_conexion():
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "")
    database = os.getenv("DB_NAME", "gestion_restaurante")
    port = int(os.getenv("DB_PORT", "3306"))

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
        print(f"No se pudo conectar a MySQL: {e}")
        return None


def conectar():
    return obtener_conexion()
