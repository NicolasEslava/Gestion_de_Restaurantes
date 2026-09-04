from modelos.mesa import Mesa
from datos.datos_mesas import (obtener_mesas, agregar_mesa, eliminar_mesa)


class MesaServicio:

    def listar_mesas(self):
        return obtener_mesas()

    def buscar_mesa(self, numero):
        mesas = obtener_mesas()

        for mesa in mesas:
            if mesa.numero == numero:
                return mesa

        return None

    def crear_mesa(self, numero):
        mesa_existente = self.buscar_mesa(numero)
        if mesa_existente is not None:
            return None

        nuevo_id = 1

        for mesa in obtener_mesas():
            if mesa.id_mesa >= nuevo_id:
                nuevo_id = mesa.id_mesa + 1

        nueva_mesa = Mesa(id_mesa=nuevo_id, numero=numero)
        agregar_mesa(nueva_mesa)
        return nueva_mesa

    def actualizar_mesa(self, numero_actual, nuevo_numero):
        mesa = self.buscar_mesa(numero_actual)

        if mesa is None:
            return None

        otra_mesa = self.buscar_mesa(nuevo_numero)

        if otra_mesa is not None and otra_mesa != mesa:
            return None

        mesa.numero = nuevo_numero

        return mesa

    def eliminar_mesa(self, numero):
        mesa = self.buscar_mesa(numero)

        if mesa is None:
            return None

        if mesa.esta_ocupada():
            return None

        eliminado = eliminar_mesa(numero)

        if eliminado:
            return mesa

        return None

    def ocupar_mesa(self, numero):
        mesa = self.buscar_mesa(numero)

        if mesa is None:
            return None

        if mesa.esta_ocupada():
            return None

        mesa.ocupar()

        return mesa

    def liberar_mesa(self, numero):
        mesa = self.buscar_mesa(numero)

        if mesa is None:
            return None

        if mesa.esta_libre():
            return None

        mesa.liberar()

        return mesa
