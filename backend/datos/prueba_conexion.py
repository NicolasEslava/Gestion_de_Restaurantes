from datos.datos_platos import obtener_platos_db


platos = obtener_platos_db()

print("Platos encontrados:")

for plato in platos:
    print(
        plato.id_plato,
        plato.nombre,
        plato.precio,
        plato.categoria,
        plato.disponible
    )
