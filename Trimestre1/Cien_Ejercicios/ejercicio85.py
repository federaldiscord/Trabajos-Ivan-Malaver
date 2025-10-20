import random

equipos = [
    {"nombre": "Tigres", "ciudad": "Monterrey", "puntos": random.randint(10, 40)},
    {"nombre": "América", "ciudad": "CDMX", "puntos": random.randint(10, 40)},
    {"nombre": "Chivas", "ciudad": "Guadalajara", "puntos": random.randint(10, 40)},
    {"nombre": "Pumas", "ciudad": "CDMX", "puntos": random.randint(10, 40)},
    {"nombre": "Cruz Azul", "ciudad": "CDMX", "puntos": random.randint(10, 40)}
]

def ordenar_por_puntos(lista):
    return sorted(lista, key=lambda e: e["puntos"], reverse=True)

def buscar_equipo(lista, nombre):
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

print("Tabla de equipos:")
for e in equipos:
    print(e["nombre"], "-", e["ciudad"], "-", e["puntos"], "pts")

print("\nEquipos ordenados por puntos:")
ordenados = ordenar_por_puntos(equipos)
for e in ordenados:
    print(e["nombre"], e["puntos"])

print("\nBúsqueda de equipo:")
equipos_ordenados_nombre = sorted(equipos, key=lambda e: e["nombre"])
indice = buscar_equipo(equipos_ordenados_nombre, "Chivas")
if indice != -1:
    print("Encontrado:", equipos_ordenados_nombre[indice])
else:
    print("No encontrado")
