import random

ciudades = [
    {"nombre": "Tokio", "poblacion": random.randint(9000000, 14000000)},
    {"nombre": "Nueva York", "poblacion": random.randint(8000000, 9000000)},
    {"nombre": "Ciudad de México", "poblacion": random.randint(8500000, 9500000)},
    {"nombre": "São Paulo", "poblacion": random.randint(11000000, 13000000)},
    {"nombre": "Londres", "poblacion": random.randint(7000000, 9000000)}
]

def ordenar_por_poblacion(lista):
    return sorted(lista, key=lambda c: c["poblacion"], reverse=True)

def buscar_ciudad(lista, nombre):
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

print("Lista de ciudades:")
for c in ciudades:
    print(c["nombre"], "-", c["poblacion"], "habitantes")

print("\nCiudades ordenadas por población:")
ordenadas = ordenar_por_poblacion(ciudades)
for c in ordenadas:
    print(c["nombre"], "-", c["poblacion"], "habitantes")

print("\nBúsqueda de ciudad:")
ciudades_ordenadas_nombre = sorted(ciudades, key=lambda c: c["nombre"])
indice = buscar_ciudad(ciudades_ordenadas_nombre, "Londres")
if indice != -1:
    print("Encontrada:", ciudades_ordenadas_nombre[indice])
else:
    print("No encontrada")
