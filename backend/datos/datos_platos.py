from modelos.plato import Plato

platos = []


def inicializar_platos():
    if len(platos) == 0:
        platos_iniciales = [
            Plato(
                id_plato=1,
                nombre="hamburguesa",
                precio=20000,
                categoria="hamburguesas"
            ),
            Plato(
                id_plato=2,
                nombre="hamburguesa doble",
                precio=280000,
                categoria="hamburguesas",
            ),
            Plato(
                id_plato=3,
                nombre="papas",
                precio=8000,
                categoria="acompañamientos",
            ),
            Plato(
                id_plato=4,
                nombre="dedos de queso",
                precio=20000,
                categoria="acompañamientos",
            ),
            Plato(
                id_plato=5,
                nombre="gaseosa",
                precio=6000,
                categoria="bebidas",
            ),
            Plato(
                id_plato=6,
                nombre="jugo natural",
                precio=12000,
                categoria="bebidas",
            ),
        ]

        platos.extend(platos_iniciales)


def obtener_platos():
    return platos


def agregar_plato(plato):
    platos.append(plato)


def eliminar_plato(id_plato):
    plato = None
    for p in platos:
        if p.id_plato == id_plato:
            plato = p
            break
    if plato is not None:
        platos.remove(plato)
        return True
    return False
