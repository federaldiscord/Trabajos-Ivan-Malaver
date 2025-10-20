def ordenar_numeros_por_insercion(lista):
    lista_ordenada = []
    for numero in lista:
        posicion = 0
        while posicion < len(lista_ordenada) and numero > lista_ordenada[posicion]:
            posicion += 1
        lista_ordenada.insert(posicion, numero)
    return lista_ordenada

numeros = [5, 2, 9, 1, 7, 4, 6, 3, 8]

print("Lista de números sin ordenar:")
print(numeros)

numeros_ordenados = ordenar_numeros_por_insercion(numeros)
print("\nLista de números ordenada por inserción:")
print(numeros_ordenados)