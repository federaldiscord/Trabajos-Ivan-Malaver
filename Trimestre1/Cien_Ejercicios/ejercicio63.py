import random
def generar_lista(n):
    return [random.randint(1, 100) for _ in range(n)]

def ordenar_lista(lista):
    return sorted(lista)

def buscar_elemento(lista, elemento):
    return elemento in lista

def generar_diccionario(n):
    return {i: i**2 for i in range(n)}

lista = generar_lista(10)
print("Lista generada:", lista)

lista_ordenada = ordenar_lista(lista)
print("Lista ordenada:", lista_ordenada)

elemento_encontrado = buscar_elemento(lista_ordenada, 5)
print("Elemento encontrado:", elemento_encontrado)

diccionario = generar_diccionario(5)
print("Diccionario generado:", diccionario)