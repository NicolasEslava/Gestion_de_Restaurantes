from datos.datos_mesas import inicializar_mesas
from servicios.mesa_servicio import MesaServicio


def mostrar_mesas(mesas):

    print("\n===== LISTA DE MESAS =====")

    for mesa in mesas:
        print(
            f"ID: {mesa.id_mesa} | "
            f"Mesa: {mesa.numero} | "
            f"Estado: {mesa.estado}"
        )


def main():

    inicializar_mesas()

    servicio = MesaServicio()

    # ==========================================
    # 1. LISTAR
    # ==========================================

    print("\n===== 1. LISTAR MESAS =====")

    mostrar_mesas(servicio.listar_mesas())

    # ==========================================
    # 2. BUSCAR
    # ==========================================

    print("\n===== 2. BUSCAR MESA 5 =====")

    mesa = servicio.buscar_mesa(5)

    if mesa:
        print(
            f"Mesa encontrada → "
            f"ID: {mesa.id_mesa} | "
            f"Mesa: {mesa.numero} | "
            f"Estado: {mesa.estado}"
        )
    else:
        print("Mesa no encontrada")

    # ==========================================
    # 3. OCUPAR
    # ==========================================

    print("\n===== 3. OCUPAR MESA 5 =====")

    mesa = servicio.ocupar_mesa(5)

    if mesa:
        print(
            f"Mesa {mesa.numero} → "
            f"Estado: {mesa.estado}"
        )
    else:
        print("No se pudo ocupar la mesa")

    # ==========================================
    # 4. INTENTAR OCUPARLA DE NUEVO
    # ==========================================

    print("\n===== 4. OCUPAR MESA 5 NUEVAMENTE =====")

    mesa = servicio.ocupar_mesa(5)

    if mesa:
        print("Mesa ocupada correctamente")
    else:
        print("No se puede ocupar: la mesa ya está ocupada")

    # ==========================================
    # 5. LIBERAR
    # ==========================================

    print("\n===== 5. LIBERAR MESA 5 =====")

    mesa = servicio.liberar_mesa(5)

    if mesa:
        print(
            f"Mesa {mesa.numero} → "
            f"Estado: {mesa.estado}"
        )
    else:
        print("No se pudo liberar la mesa")

    # ==========================================
    # 6. CREAR
    # ==========================================

    print("\n===== 6. CREAR MESA 13 =====")

    mesa = servicio.crear_mesa(13)

    if mesa:
        print(
            f"Mesa creada → "
            f"ID: {mesa.id_mesa} | "
            f"Mesa: {mesa.numero} | "
            f"Estado: {mesa.estado}"
        )
    else:
        print("No se pudo crear la mesa")

    # ==========================================
    # 7. INTENTAR CREAR DUPLICADA
    # ==========================================

    print("\n===== 7. CREAR MESA 13 NUEVAMENTE =====")

    mesa = servicio.crear_mesa(13)

    if mesa:
        print("Mesa creada")
    else:
        print("No se puede crear: la mesa 13 ya existe")

    # ==========================================
    # 8. ACTUALIZAR
    # ==========================================

    print("\n===== 8. ACTUALIZAR MESA 13 → 20 =====")

    mesa = servicio.actualizar_mesa(13, 20)

    if mesa:
        print(
            f"Mesa actualizada → "
            f"ID: {mesa.id_mesa} | "
            f"Nuevo número: {mesa.numero} | "
            f"Estado: {mesa.estado}"
        )
    else:
        print("No se pudo actualizar la mesa")

    # ==========================================
    # 9. ELIMINAR
    # ==========================================

    print("\n===== 9. ELIMINAR MESA 20 =====")

    mesa = servicio.eliminar_mesa(20)

    if mesa:
        print(
            f"Mesa {mesa.numero} eliminada correctamente"
        )
    else:
        print("No se pudo eliminar la mesa")

    # ==========================================
    # 10. LISTADO FINAL
    # ==========================================

    print("\n===== 10. ESTADO FINAL =====")

    mostrar_mesas(servicio.listar_mesas())


if __name__ == "__main__":
    main()
