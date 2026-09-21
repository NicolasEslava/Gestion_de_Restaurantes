from modelos.mesa import Mesa
from datos.datos_mesas import (
    obtener_mesas_db, buscar_mesa_db, crear_mesa_db, actualizar_mesa_db, eliminar_mesa_db, ocupar_mesa_db, liberar_mesa_db)


class MesaServicio:

    def listar_mesas(self):
        mesas_db = obtener_mesas_db()

        mesas = []

        for mesa in mesas_db:
            nueva_mesa = Mesa(
                id_mesa=mesa["id_mesa"],
                numero=mesa["numero"]
            )

            if mesa["estado"] == "ocupada":
                nueva_mesa.ocupar()

            mesas.append(nueva_mesa)

        return mesas

    def buscar_mesa(self, numero):
        mesa_db = buscar_mesa_db(numero)

        if mesa_db is None:
            return None

        mesa = Mesa(
            id_mesa=mesa_db["id_mesa"],
            numero=mesa_db["numero"]
        )

        if mesa_db["estado"] == "ocupada":
            mesa.ocupar()

        return mesa

    def crear_mesa(self, numero):

        mesa_existente = self.buscar_mesa(numero)

        if mesa_existente is not None:
            return None

        id_mesa = crear_mesa_db(numero)

        return Mesa(
            id_mesa=id_mesa,
            numero=numero
        )

    def actualizar_mesa(self, numero_actual, nuevo_numero):

        mesa = self.buscar_mesa(numero_actual)

        if mesa is None:
            return None

        otra_mesa = self.buscar_mesa(nuevo_numero)

        if otra_mesa is not None and otra_mesa.numero != numero_actual:
            return None

        filas_afectadas = actualizar_mesa_db(
            numero_actual,
            nuevo_numero
        )

        if filas_afectadas == 0:
            return None

        mesa.numero = nuevo_numero

        return mesa

    def eliminar_mesa(self, numero):

        mesa = self.buscar_mesa(numero)

        if mesa is None:
            return None

        if mesa.esta_ocupada():
            return None

        filas_afectadas = eliminar_mesa_db(numero)

        if filas_afectadas == 0:
            return None

        return mesa

    def ocupar_mesa(self, numero):

        mesa = self.buscar_mesa(numero)

        if mesa is None:
            return None

        if mesa.esta_ocupada():
            return None

        filas_afectadas = ocupar_mesa_db(numero)

        if filas_afectadas == 0:
            return None

        mesa.ocupar()

        return mesa

    def liberar_mesa(self, numero):

        mesa = self.buscar_mesa(numero)

        if mesa is None:
            return None

        if mesa.esta_libre():
            return None

        filas_afectadas = liberar_mesa_db(numero)

        if filas_afectadas == 0:
            return None

        mesa.liberar()

        return mesa
