import random

peliculas = [
    {"titulo": "Inception", "director": "Christopher Nolan", "calificacion": random.randint(1, 10)},
    {"titulo": "Titanic", "director": "James Cameron", "calificacion": random.randint(1, 10)},
    {"titulo": "The Matrix", "director": "Lana y Lilly Wachowski", "calificacion": random.randint(1, 10)},
    {"titulo": "Parasite", "director": "Bong Joon-ho", "calificacion": random.randint(1, 10)},
    {"titulo": "Interstellar", "director": "Christopher Nolan", "calificacion": random.randint(1, 10)}
]

def ordenar_por_calificacion(lista):
    return sorted(lista, key=lambda p: p["calificacion"], reverse=True)

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
    print(p["titulo"], "-", p["director"], "-", p["calificacion"], "⭐")

print("\nPelículas ordenadas por calificación:")
ordenadas = ordenar_por_calificacion(peliculas)
for p in ordenadas:
    print(p["titulo"], p["calificacion"])

print("\nBúsqueda de película:")
peliculas_ordenadas_titulo = sorted(peliculas, key=lambda p: p["titulo"])
indice = buscar_pelicula(peliculas_ordenadas_titulo, "Titanic")
if indice != -1:
    print("Encontrada:", peliculas_ordenadas_titulo[indice])
else:
    print("No encontrada")
