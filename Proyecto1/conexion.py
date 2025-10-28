import psycopg2
connextion = psycopg2.connect(
        host="localhost",
        database="proyecto1",
        user="postgres",
        password="MkUltra#2026",
        port="5432"
    )
print(connextion)
print("Conexión exitosa a la base de datos")
