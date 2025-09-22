def encontrar_numero_menor(lista):
    numero_menor = lista[0]
    for numero in lista:
        if numero < numero_menor:
            numero_menor = numero
    return numero_menor

numeros = [5, 2, 9, 1, 7, 4, 6, 3, 8]

print("Lista de números:")
print(numeros)

numero_menor = encontrar_numero_menor(numeros)
print("\nNúmero más pequeño en la lista:", numero_menor)