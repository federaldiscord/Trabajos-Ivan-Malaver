import random

ciudades = [
    {"nombre": "Tokio", "poblacion": 37400000},
    {"nombre": "Nueva York", "poblacion": 19300000},
    {"nombre": "Ciudad de México", "poblacion": 21900000},
    {"nombre": "São Paulo", "poblacion": 22000000},
    {"nombre": "París", "poblacion": 11000000}
]

def ordenar_por_poblacion(lista):
    return sorted(lista, key=lambda x: x["poblacion"], reverse=True)

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
ciudades_ordenadas_nombre = sorted(ciudades, key=lambda x: x["nombre"])
indice = buscar_ciudad(ciudades_ordenadas_nombre, "París")
if indice != -1:
    print("Encontrada:", ciudades_ordenadas_nombre[indice])
else:
    print("No encontrada")
