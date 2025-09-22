import random

universidades = [
    {"nombre": "Harvard", "pais": "EE.UU.", "ranking": random.randint(1, 50)},
    {"nombre": "Oxford", "pais": "Reino Unido", "ranking": random.randint(1, 50)},
    {"nombre": "MIT", "pais": "EE.UU.", "ranking": random.randint(1, 50)},
    {"nombre": "Cambridge", "pais": "Reino Unido", "ranking": random.randint(1, 50)},
    {"nombre": "Stanford", "pais": "EE.UU.", "ranking": random.randint(1, 50)}
]

def ordenar_por_ranking(lista):
    return sorted(lista, key=lambda u: u["ranking"])

def buscar_universidad(lista, nombre):
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

print("Lista de universidades:")
for u in universidades:
    print(u["nombre"], "-", u["pais"], "- Ranking:", u["ranking"])

print("\nUniversidades ordenadas por ranking:")
ordenadas = ordenar_por_ranking(universidades)
for u in ordenadas:
    print(u["nombre"], u["ranking"])

print("\nBúsqueda de universidad:")
universidades_ordenadas_nombre = sorted(universidades, key=lambda u: u["nombre"])
indice = buscar_universidad(universidades_ordenadas_nombre, "MIT")
if indice != -1:
    print("Encontrada:", universidades_ordenadas_nombre[indice])
else:
    print("No encontrada")
