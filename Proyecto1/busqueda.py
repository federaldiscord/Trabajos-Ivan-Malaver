from conexion import connextion
apuntador = connextion.cursor()


apuntador.execute("SELECT * FROM reg_datos")
registros = apuntador.fetchall()
print(registros)