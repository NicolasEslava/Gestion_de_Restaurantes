class Usuario:
    def __init__(self, id_usuario, usuario, nombre, rol):
        self.id_usuario = id_usuario
        self.usuario = usuario
        self.nombre = nombre
        self.rol = rol  # 'admin' o 'mesero'

    def es_admin(self):
        return self.rol == 'admin'

    def es_mesero(self):
        return self.rol == 'mesero'