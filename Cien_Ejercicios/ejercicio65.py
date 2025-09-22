import time
import random

def generar_matriz(n):
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def ordenar_matriz_seleccion(n):
    matriz = generar_matriz(n)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if matriz[j][i] < matriz[min_idx][i]:
                min_idx = j
        matriz[i], matriz[min_idx] = matriz[min_idx], matriz[i]
    return matriz

def buscar_en_anchura(grafo, inicio, destino):
    visitados = set()
    cola = [(inicio, 0)]
    while cola:
        nodo, distancia = cola.pop(0)
        if nodo not in visitados:
            visitados.add(nodo)
            if nodo == destino:
                return distancia
            for vecino in grafo[nodo]:
                cola.append((vecino, distancia + 1))
    return -1

n = 5
matriz = ordenar_matriz_seleccion(n)
print("Matriz ordenada:")
imprimir_matriz(matriz)

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

inicio = 'A'
destino = 'E'
tiempo_inicio = time.time()
distancia = buscar_en_anchura(grafo, inicio, destino)
tiempo_final = time.time()
print("Distancia en la búsqueda en anchura:", distancia)
print("Tiempo de ejecución:", tiempo_final - tiempo_inicio, "segundos")