import random

ciudades = [
    ("Madrid", {"poblacion": 3200000, "distancia": random.randint(100, 1000)}),
    ("Barcelona", {"poblacion": 1600000, "distancia": random.randint(100, 1000)}),
    ("Valencia", {"poblacion": 800000, "distancia": random.randint(100, 1000)}),
    ("Sevilla", {"poblacion": 700000, "distancia": random.randint(100, 1000)}),
    ("Bilbao", {"poblacion": 345000, "distancia": random.randint(100, 1000)})
]

def ordenar_por_poblacion(lista):
    return sorted(lista, key=lambda c: c[1]["poblacion"], reverse=True)

def buscar_ciudad(lista, nombre):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][0].lower() == nombre.lower():
            return medio
        elif lista[medio][0].lower() < nombre.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

print("Ciudades registradas:")
for c in ciudades:
    print(c[0], "- Población:", c[1]["poblacion"], "- Distancia:", c[1]["distancia"], "km")

print("\nCiudades ordenadas por población:")
ordenadas = ordenar_por_poblacion(ciudades)
for c in ordenadas:
    print(c[0], c[1]["poblacion"])

print("\nBúsqueda de ciudad:")
ciudades_ordenadas_nombre = sorted(ciudades, key=lambda c: c[0])
indice = buscar_ciudad(ciudades_ordenadas_nombre, "Sevilla")
if indice != -1:
    print("Encontrada:", ciudades_ordenadas_nombre[indice])
else:
    print("No encontrada")
