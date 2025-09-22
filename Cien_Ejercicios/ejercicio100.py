import random

planetas = [
    {"nombre": "Mercurio", "distancia": 58},
    {"nombre": "Venus", "distancia": 108},
    {"nombre": "Tierra", "distancia": 150},
    {"nombre": "Marte", "distancia": 228},
    {"nombre": "Júpiter", "distancia": 778},
    {"nombre": "Saturno", "distancia": 1430},
    {"nombre": "Urano", "distancia": 2870},
    {"nombre": "Neptuno", "distancia": 4490}
]

def ordenar_por_distancia(lista):
    return sorted(lista, key=lambda x: x["distancia"])

def buscar_planeta(lista, nombre):
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

print("Lista de planetas:")
for p in planetas:
    print(p["nombre"], "-", p["distancia"], "millones de km")

print("\nPlanetas ordenados por distancia al Sol:")
ordenados = ordenar_por_distancia(planetas)
for p in ordenados:
    print(p["nombre"], "-", p["distancia"], "millones de km")

print("\nBúsqueda de planeta:")
planetas_ordenados_nombre = sorted(planetas, key=lambda x: x["nombre"])
indice = buscar_planeta(planetas_ordenados_nombre, "Marte")
if indice != -1:
    print("Encontrado:", planetas_ordenados_nombre[indice])
else:
    print("No encontrado")
