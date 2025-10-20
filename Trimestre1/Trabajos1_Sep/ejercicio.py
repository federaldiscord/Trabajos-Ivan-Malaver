lista = [1, 10, 15, 20, 30, 40, 50, 7, 20]

def saludar(nombre):
    print("Hola python saludo " + nombre)
saludar("Carlos")


diccionario = [
    {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 25, "ciudad": "Bogotá"},
    {"nombre": "Luis", "edad": 28, "ciudad": "Funza"},
    {"nombre": "Marta", "edad": 32, "ciudad": "Mosquera"},
    {"nombre": "Javier", "edad": 27, "ciudad": "Soacha"}
]
for persona in diccionario:
    print(persona["nombre"], persona["edad"], persona["ciudad"])