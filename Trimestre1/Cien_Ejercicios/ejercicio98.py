import random

coches = [
    {"nombre": "Ferrari F8", "velocidad_max": 340},
    {"nombre": "Bugatti Chiron", "velocidad_max": 420},
    {"nombre": "Lamborghini Aventador", "velocidad_max": 350},
    {"nombre": "Porsche 911", "velocidad_max": 330},
    {"nombre": "McLaren 720S", "velocidad_max": 341}
]

def ordenar_por_velocidad(lista):
    return sorted(lista, key=lambda x: x["velocidad_max"], reverse=True)

def buscar_coche(lista, nombre):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio]["nombre"].lower() == nombre.lower():
            return medio
        elif lista[medio]["nombre"].lower() < nombre.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

print("Lista de coches:")
for c in coches:
    print(c["nombre"], "-", c["velocidad_max"], "km/h")

print("\nCoches ordenados por velocidad máxima:")
ordenados = ordenar_por_velocidad(coches)
for c in ordenados:
    print(c["nombre"], "-", c["velocidad_max"], "km/h")

print("\nBúsqueda de coche:")
coches_ordenados_nombre = sorted(coches, key=lambda x: x["nombre"])
indice = buscar_coche(coches_ordenados_nombre, "Porsche 911")
if indice != -1:
    print("Encontrado:", coches_ordenados_nombre[indice])
else:
    print("No encontrado")
