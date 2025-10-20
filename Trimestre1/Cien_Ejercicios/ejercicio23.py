def encontrar_suma_numeros_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma

numeros = [5, 2, 9, 1, 7, 4, 6, 3, 8]

print("Lista de números:")
print(numeros)

suma_numeros_pares = encontrar_suma_numeros_pares(numeros)
print("\nSuma de los números pares en la lista:", suma_numeros_pares)