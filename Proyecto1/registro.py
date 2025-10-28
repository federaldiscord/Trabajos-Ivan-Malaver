from conexion import connextion

humedad = input("Ingrese el valor de humedad dado por el sensor: ")
cantidad_hectareas = input("Confirme la cantidad de hectareas: ")
usuario = input("Ingrese su nombre para asociarlo al registro: ")

apuntador = connextion.cursor()
apuntador.execute(" CREATE TABLE IF NOT EXISTS reg_datos (id SERIAL PRIMARY KEY, humedad VARCHAR(100), hectareas VARCHAR(100), usuario VARCHAR(100))")
apuntador.execute("INSERT INTO reg_datos (humedad, hectareas, usuario) VALUES (%s, %s, %s)", (humedad, cantidad_hectareas, usuario))
connextion.commit()
print("Datos insertados correctamente")
apuntador.close()
connextion.close()



