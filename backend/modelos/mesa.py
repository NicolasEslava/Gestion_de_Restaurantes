class Mesa:
    def __init__(self, id_mesa, numero, estado="libre"):
        self.id_mesa = id_mesa
        self.numero = numero
        self.estado = estado

    def ocupar(self):
        self.estado = "ocupada"

    def liberar(self):
        self.estado = "libre"

    def esta_libre(self):
        return self.estado == "libre"

    def esta_ocupada(self):
        return self.estado == "ocupada"
