from modelos.mesa import Mesa

mesas = []


def inicializar_mesas():
    if len(mesas) == 0:
        for numero in range(1, 13):
            mesa = Mesa(id_mesa=numero, numero=numero)
            mesas.append(mesa)


def obtener_mesas():
    return mesas


def agregar_mesa(mesa):
    mesas.append(mesa)


def eliminar_mesa(numero):
    mesa = None
    for m in mesas:
        if m.numero == numero:
            mesa = m
            break

    if mesa is not None:
        mesas.remove(mesa)
        return True
    return False
