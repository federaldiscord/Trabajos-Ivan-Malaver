import random

def generar_lista_numeros(n):
    """Genera una lista de n números enteros aleatorios (1 a 100)."""
    return [random.randint(1, 100) for _ in range(n)]

def imprimir_lista_numeros(lista):
    """Imprime la lista de números en una sola línea."""
    print(lista, "\n")

def ordenar_lista_mezcla_numeros(lista):
    """Ordena una lista de números con Merge Sort."""
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = ordenar_lista_mezcla_numeros(lista[:medio])
    derecha = ordenar_lista_mezcla_numeros(lista[medio:])
    return mezclar(izquierda, derecha)

def mezclar(izquierda, derecha):
    """Mezcla dos listas ordenadas en una sola lista ordenada."""
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1
    return resultado

def buscar_binaria_numeros(lista, numero):
    """Búsqueda binaria en una lista ordenada de números."""
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == numero:
            return medio
        elif lista[medio] < numero:
            inicio = medio + 1
        else:
            final = medio - 1
    return -1

n = 10
lista_numeros = generar_lista_numeros(n)
print("Lista de números generada:")
imprimir_lista_numeros(lista_numeros)

lista_numeros_ordenada = ordenar_lista_mezcla_numeros(lista_numeros)
print("Lista de números ordenada:")
imprimir_lista_numeros(lista_numeros_ordenada)

numero = 75
indice = buscar_binaria_numeros(lista_numeros_ordenada, numero)
if indice != -1:
    print(f"El número {numero} se encontró en el índice {indice}.")
else:
    print(f"El número {numero} no está en la lista.")
