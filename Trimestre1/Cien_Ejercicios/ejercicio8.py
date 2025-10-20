def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

numeros = [5, 2, 9, 1, 7, 4, 6, 3, 8]

print("Lista de números sin ordenar:")
print(numeros)

lista_invertida = invertir_lista(numeros)
print("\nLista de números invertida:")
print(lista_invertida)