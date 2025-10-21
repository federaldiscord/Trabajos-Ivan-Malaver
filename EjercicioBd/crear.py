import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="proyecto1",
        user="postgres",
        password="MkUltra#2026",
        port="5432"
    )
print(conn)
print("Conexión exitosa a la base de datos")

nombre = input("Ingrese el nombre del usuario: ")
apellido = input("Ingrese el apellido del usuario: ")
cedula = input("Ingrese la cédula del usuario: ")

cursor = conn.cursor()
cursor.execute(" CREATE TABLE IF NOT EXISTS usuarios (id SERIAL PRIMARY KEY, nombre VARCHAR(20), apellido VARCHAR(20), cedula VARCHAR(11)); INSERT INTO usuarios (nombre, apellido, cedula) VALUES (%s, %s, %s)", (nombre, apellido, cedula))
conn.commit()
print("Datos insertados correctamente")
cursor.close()
conn.close()



