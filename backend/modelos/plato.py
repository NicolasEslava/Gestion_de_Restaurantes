class Plato:
    def __init__(self, id_plato, nombre, precio, categoria, disponible=True):
        self.id_plato = id_plato
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible

    def activar(self):
        self.disponible = True

    def desactivar(self):
        self.disponible = False

    def esta_disponible(self):
        return self.disponible
