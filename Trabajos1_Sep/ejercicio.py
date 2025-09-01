lista = [1, 10, 15, 20, 30, 40, 50, 7, 20]

def saludar(nombre):
    print("Hola python saludo " + nombre)
saludar("Carlos")

diccionarios = {
    "diccionario1": {
        "nombre": "Carlos",
        "edad": 30,
        "ciudad": "Madrid",
    },
    "diccionario2": {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Barcelona",
    },
    "diccionario3": {
        "nombre": "Luis",
        "edad": 28,
        "ciudad": "Valencia",
    },
    "diccionario4": {
        "nombre": "Marta",
        "edad": 32,
        "ciudad": "Sevilla",
    },
    "diccionario5": {
        "nombre": "Javier",
        "edad": 27,
        "ciudad": "Bilbao",
    }
}

diccionario = diccionarios["diccionario1"]
print(diccionario["nombre"], diccionario["edad"], diccionario["ciudad"])