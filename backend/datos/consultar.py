from backend.datos.conexion import conectar

conexion = conectar()

cursor = conexion.cursor()

cursor.execute("SELECT * FROM mesas")

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

cursor.close()
conexion.close()
