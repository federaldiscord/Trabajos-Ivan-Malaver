import random

deportes = [
    {"nombre": "Fútbol", "jugadores": 11},
    {"nombre": "Baloncesto", "jugadores": 5},
    {"nombre": "Béisbol", "jugadores": 9},
    {"nombre": "Rugby", "jugadores": 15},
    {"nombre": "Voleibol", "jugadores": 6}
]

def ordenar_por_jugadores(lista):
    return sorted(lista, key=lambda d: d["jugadores"])

def buscar_deporte(lista, nombre):
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

print("Lista de deportes:")
for d in deportes:
    print(d["nombre"], "-", d["jugadores"], "jugadores por equipo")

print("\nDeportes ordenados por número de jugadores:")
ordenados = ordenar_por_jugadores(deportes)
for d in ordenados:
    print(d["nombre"], "-", d["jugadores"], "jugadores por equipo")

print("\nBúsqueda de deporte:")
deportes_ordenados_nombre = sorted(deportes, key=lambda d: d["nombre"])
indice = buscar_deporte(deportes_ordenados_nombre, "Rugby")
if indice != -1:
    print("Encontrado:", deportes_ordenados_nombre[indice])
else:
    print("No encontrado")
