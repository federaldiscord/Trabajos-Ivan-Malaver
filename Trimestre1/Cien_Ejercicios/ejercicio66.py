import time
import random

def generar_lista(n):
    return [random.randint(1, 100) for _ in range(n)]

def imprimir_lista(lista):
    print(lista)

def ordenar_lista_insercion(lista):
    n = len(lista)
    for i in range(1, n):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = clave
    return lista

def buscar_binaria(lista, elemento):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            final = medio - 1
    return -1

n = 10
lista = generar_lista(n)
print("Lista generada:")
imprimir_lista(lista)

lista_ordenada = ordenar_lista_insercion(lista)
print("Lista ordenada:")
imprimir_lista(lista_ordenada)

elemento = 75
indice = buscar_binaria(lista_ordenada, elemento)
print("Índice del elemento:", indice)