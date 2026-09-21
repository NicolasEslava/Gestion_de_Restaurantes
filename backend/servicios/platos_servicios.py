from modelos.plato import Plato
from datos.datos_platos import (
    eliminar_plato_db, obtener_platos_db, buscar_plato_db, crear_plato_db, actualizar_plato_db)


class Platoservicio:
    def listar_platos(self):
        return obtener_platos_db()

    def buscar_plato(self, id_plato):
        producto = buscar_plato_db(id_plato)

        if producto is None:
            return None

        return Plato(
            id_plato=producto["id_producto"],
            nombre=producto["nombre_producto"],
            precio=producto["precio"],
            categoria=producto["categoria"],
            disponible=producto["estado"] == "disponible"
        )

    def crear_plato(self, nombre, precio, categoria):
        id_plato = crear_plato_db(nombre, precio, categoria)

        return Plato(
            id_plato=id_plato,
            nombre=nombre,
            precio=precio,
            categoria=categoria
        )

    def actualizar_plato(self, id_plato, nombre=None, precio=None, categoria=None, disponible=None):
        plato = self.buscar_plato(id_plato)

        if plato is None:
            return None

        if nombre is None:
            nombre = plato.nombre

        if precio is None:
            precio = plato.precio

        if categoria is None:
            categoria = plato.categoria

        if disponible is None:
            disponible = plato.disponible

        filas_afectadas = actualizar_plato_db(
            id_plato,
            nombre,
            precio,
            categoria,
            disponible
        )

        if filas_afectadas == 0:
            return None

        return self.buscar_plato(id_plato)

    def eliminar_plato(self, id_plato):
        plato = self.buscar_plato(id_plato)

        if plato is None:
            return None

        filas_afectadas = eliminar_plato_db(id_plato)

        if filas_afectadas == 0:
            return None

        return plato
