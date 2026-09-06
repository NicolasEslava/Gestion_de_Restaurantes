from modelos.plato import Plato
from datos.datos_platos import (obtener_platos, agregar_plato, eliminar_plato)


class Platoservicio:
    def listar_platos(self):
        return obtener_platos()

    def buscar_plato(self, id_plato):
        platos = obtener_platos()
        for plato in platos:
            if plato.id_plato == id_plato:
                return plato
        return None

    def crear_plato(self, nombre, precio, categoria):
        nuevo_id = 1
        for plato in obtener_platos():
            if plato.id_plato >= nuevo_id:
                nuevo_id = plato.id_palto + 1

        nuevo_plato = Plato(
            id_plato=nuevo_id,
            nombre=nombre,
            precio=precio,
            categoria=categoria
        )
        agregar_plato(nuevo_plato)
        return nuevo_plato

    def actualizar_plato(self, id_plato, nombre=None, precio=None, categoria=None, disponible=None):
        plato = self.buscar_plato(id_plato)
        if plato is None:
            return None

        if nombre is not None:
            plato.nombre = nombre

        if precio is not None:
            plato.precio = precio

        if categoria is not None:
            plato.categoria = categoria

        if disponible is not None:
            plato.disponible = disponible

        return plato

    def eliminar_plato(self, id_plato):

        plato = self.buscar_plato(id_plato)

        if plato is None:
            return None

        eliminado = eliminar_plato(id_plato)

        if eliminado:
            return plato

        return None
