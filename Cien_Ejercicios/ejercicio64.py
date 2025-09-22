import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def insertar_elemento_en_lista_enlazada(lista, valor):
    nuevo_nodo = Nodo(valor)
    if lista is None:
        lista = nuevo_nodo
    else:
        actual = lista
        while actual.siguiente is not None and actual.valor < valor:
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
    return lista

def buscar_elemento_en_lista_enlazada(lista, valor):
    actual = lista
    while actual is not None:
        if actual.valor == valor:
            return True
        actual = actual.siguiente
    return False

def generar_diccionario(n):
    return {i: i**2 for i in range(n)}

def buscar_en_profundidad(raiz, valor):
    if raiz is None:
        return False
    if raiz.valor == valor:
        return True
    return buscar_en_profundidad(raiz.izquierda, valor) or buscar_en_profundidad(raiz.derecha, valor)

lista_enlazada = None
valor = 5
lista_enlazada = insertar_elemento_en_lista_enlazada(lista_enlazada, valor)
print("Lista enlazada:", end=" ")
actual = lista_enlazada
while actual is not None:
    print(actual.valor, end=" ")
    actual = actual.siguiente
print()

elemento_encontrado = buscar_elemento_en_lista_enlazada(lista_enlazada, valor)
print("Elemento encontrado en la lista enlazada:", elemento_encontrado)

diccionario = generar_diccionario(5)
print("Diccionario generado:", diccionario)

raiz = None
valor_a_buscar = 6
encontrado = buscar_en_profundidad(raiz, valor_a_buscar)
print("Elemento encontrado en el árbol binario:", encontrado)