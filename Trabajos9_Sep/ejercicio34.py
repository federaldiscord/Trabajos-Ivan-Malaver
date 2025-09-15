import random
import math
from itertools import permutations

def calcular_distancia(ciudad1, ciudad2):
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distancia, 2)

def calcular_distancia_total_ruta(ciudades, ruta):
    distancia_total = 0
    for i in range(len(ruta)):
        ciudad_actual = ciudades[ruta[i]]
        siguiente_ciudad = ciudades[ruta[(i + 1) % len(ruta)]]
        distancia = calcular_distancia(ciudad_actual, siguiente_ciudad)
        distancia_total += distancia
    return round(distancia_total, 2)

def metodo_fuerza_bruta(ciudades):
    num_ciudades = len(ciudades)
    mejor_ruta = None
    mejor_distancia = float("inf")
    for ruta in permutations(range(num_ciudades)):
        distancia = calcular_distancia_total_ruta(ciudades, ruta)
        if distancia < mejor_distancia:
            mejor_distancia = distancia
            mejor_ruta = ruta
    return mejor_ruta, mejor_distancia

def generar_ciudades(n, max_coord=100):
    return [(random.randint(0, max_coord), random.randint(0, max_coord)) for _ in range(n)]

if __name__ == "__main__":
    ciudades = generar_ciudades(5)
    print("Ciudades:")
    for i, c in enumerate(ciudades):
        print(f"Ciudad {i}: {c}")
    mejor_ruta, mejor_distancia = metodo_fuerza_bruta(ciudades)
    print("\nMejor ruta encontrada:")
    print(" -> ".join(str(i) for i in mejor_ruta))
    print(f"Distancia total: {mejor_distancia}")
