import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

from passlib.context import CryptContext
from data_base.conexion import obtener_conexion

contexto_contrasenas = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_contrasena(contrasena: str, hash_contrasena: str) -> bool:
    return contexto_contrasenas.verify(contrasena, hash_contrasena)

def autenticar_usuario(usuario: str, contrasena_ingresada: str):
    conexion = obtener_conexion()
    if conexion is None:
        return None

    try:
        cursor = conexion.cursor(dictionary=True)
        query = """
            SELECT id, username AS usuario, password_hash AS hash_contrasena,
                   nombre, rol
            FROM usuarios 
            WHERE username = %s AND estado = TRUE
        """
        cursor.execute(query, (usuario,))
        registro_usuario = cursor.fetchone()
        cursor.close()

        if not registro_usuario:
            return None

        if not verificar_contrasena(
            contrasena_ingresada, registro_usuario["hash_contrasena"]
        ):
            return None

        return {
            "id": registro_usuario["id"],
            "usuario": registro_usuario["usuario"],
            "nombre": registro_usuario["nombre"],
            "rol": registro_usuario["rol"]
        }
    except Exception as e:
        print(f"Error en la consulta: {e}")
        return None
    finally:
        if conexion and conexion.is_connected():
            conexion.close()