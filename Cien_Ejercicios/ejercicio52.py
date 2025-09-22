def ordenar_numeros(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

numeros = [5, 2, 9, 1, 7, 4, 6, 3, 8]

print("Lista de números sin ordenar:")
print(numeros)

numeros_ordenados = ordenar_numeros(numeros)
print("\nLista de números ordenada de menor a mayor:")
print(numeros_ordenados)