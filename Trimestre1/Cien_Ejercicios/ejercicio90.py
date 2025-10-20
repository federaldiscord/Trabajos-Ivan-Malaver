import random

videojuegos = [
    {"titulo": "The Legend of Zelda", "puntuacion": random.randint(80, 100)},
    {"titulo": "Elden Ring", "puntuacion": random.randint(85, 100)},
    {"titulo": "Minecraft", "puntuacion": random.randint(70, 95)},
    {"titulo": "God of War", "puntuacion": random.randint(85, 100)},
    {"titulo": "Super Mario Odyssey", "puntuacion": random.randint(80, 98)}
]

def ordenar_por_puntuacion(lista):
    return sorted(lista, key=lambda v: v["puntuacion"], reverse=True)

def buscar_videojuego(lista, titulo):
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

print("Lista de videojuegos:")
for v in videojuegos:
    print(v["titulo"], "-", v["puntuacion"], "puntos")

print("\nVideojuegos ordenados por puntuación:")
ordenados = ordenar_por_puntuacion(videojuegos)
for v in ordenados:
    print(v["titulo"], "-", v["puntuacion"], "puntos")

print("\nBúsqueda de videojuego:")
videojuegos_ordenados_titulo = sorted(videojuegos, key=lambda v: v["titulo"])
indice = buscar_videojuego(videojuegos_ordenados_titulo, "Minecraft")
if indice != -1:
    print("Encontrado:", videojuegos_ordenados_titulo[indice])
else:
    print("No encontrado")
