import random

peliculas = [
    {"titulo": "Inception", "duracion": random.randint(120, 160)},
    {"titulo": "Interstellar", "duracion": random.randint(150, 180)},
    {"titulo": "The Dark Knight", "duracion": random.randint(140, 165)},
    {"titulo": "Parasite", "duracion": random.randint(120, 140)},
    {"titulo": "Gladiator", "duracion": random.randint(150, 175)}
]

def ordenar_por_duracion(lista):
    return sorted(lista, key=lambda p: p["duracion"])

def buscar_pelicula(lista, titulo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio]["titulo"].lower() == titulo.lower():
            return medio
        elif lista[medio]["titulo"].lower() < titulo.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

print("Lista de películas:")
for p in peliculas:
    print(p["titulo"], "-", p["duracion"], "minutos")

print("\nPelículas ordenadas por duración:")
ordenadas = ordenar_por_duracion(peliculas)
for p in ordenadas:
    print(p["titulo"], "-", p["duracion"], "minutos")

print("\nBúsqueda de película:")
peliculas_ordenadas_titulo = sorted(peliculas, key=lambda p: p["titulo"])
indice = buscar_pelicula(peliculas_ordenadas_titulo, "Inception")
if indice != -1:
    print("Encontrada:", peliculas_ordenadas_titulo[indice])
else:
    print("No encontrada")
