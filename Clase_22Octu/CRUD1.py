import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="practicas_crud",
        user="postgres",
        password="MkUltra#2026",
        port="5432"
    )
print(conn)
print("Conexión exitosa a la base de datos")

