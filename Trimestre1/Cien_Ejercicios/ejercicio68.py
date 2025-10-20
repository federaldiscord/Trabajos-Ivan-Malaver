import random

def generar_lista_palabras(n):
    """Genera una lista de n palabras aleatorias (de 3 a 8 letras)."""
    palabras = []
    for _ in range(n):
        palabra = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(3, 8)))
        palabras.append(palabra)
    return palabras

def imprimir_lista_palabras(lista):
    """Imprime cada palabra en la lista."""
    for palabra in lista:
        print(palabra)
    print()

def ordenar_lista_insercion_palabras(lista):
    """Ordena una lista de palabras usando el método de inserción."""
    n = len(lista)
    for i in range(1, n):
        palabra = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > palabra:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = palabra
    return lista

def buscar_binaria_palabras(lista, palabra):
    """Búsqueda binaria en una lista ordenada de palabras."""
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == palabra:
            return medio
        elif lista[medio] < palabra:
            inicio = medio + 1
        else:
            final = medio - 1
    return -1

n = 10
lista_palabras = generar_lista_palabras(n)
print("Lista de palabras generada:")
imprimir_lista_palabras(lista_palabras)

lista_palabras_ordenada = ordenar_lista_insercion_palabras(lista_palabras[:])
print("Lista de palabras ordenada:")
imprimir_lista_palabras(lista_palabras_ordenada)

palabra = "banana"
indice = buscar_binaria_palabras(lista_palabras_ordenada, palabra)
if indice != -1:
    print(f"La palabra '{palabra}' se encontró en el índice {indice}.")
else:
    print(f"La palabra '{palabra}' no está en la lista.")
