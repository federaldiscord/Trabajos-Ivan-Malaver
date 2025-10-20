import random
import time

def generar_grafo_no_dirigido(n, m):
    grafo = {}
    for i in range(n):
        grafo[i] = set()
    for _ in range(m):
        nodo1 = random.randint(0, n-1)
        nodo2 = random.randint(0, n-1)
        if nodo1 != nodo2:
            grafo[nodo1].add(nodo2)
            grafo[nodo2].add(nodo1)
    return grafo

def imprimir_grafo_no_dirigido(grafo):
    for nodo in grafo:
        adyacencias = grafo[nodo]
        print("Nodo:", nodo)
        print("Adyacencias:", adyacencias)
        print()

def buscar_en_profundidad(grafo, nodo, visitados):
    visitados.add(nodo)
    for adyacente in grafo[nodo]:
        if adyacente not in visitados:
            buscar_en_profundidad(grafo, adyacente, visitados)
    return visitados

n = 5
m = 6
grafo = generar_grafo_no_dirigido(n, m)
print("Grafo no dirigido generado:")
imprimir_grafo_no_dirigido(grafo)

visitados = set()
nodo_inicial = 0
visitados = buscar_en_profundidad(grafo, nodo_inicial, visitados)
print("Nodos visitados en la búsqueda en profundidad:", visitados)