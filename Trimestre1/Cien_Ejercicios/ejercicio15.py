def encontrar_numero_mayor(lista):
    numero_mayor = lista[0]
    for numero in lista:
        if numero > numero_mayor:
            numero_mayor = numero
    return numero_mayor

numeros = [5, 2, 9, 1, 7, 4, 6, 3, 8]

print("Lista de números:")
print(numeros)

numero_mayor = encontrar_numero_mayor(numeros)
print("\nNúmero mayor en la lista:", numero_mayor)