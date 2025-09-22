def encontrar_numero_mas_grande(lista):
    numero_mas_grande = lista[0]
    for numero in lista:
        if numero > numero_mas_grande:
            numero_mas_grande = numero
    return numero_mas_grande

numeros = [5, 2, 9, 1, 7, 4, 6, 3, 8]

print("Lista de números:")
print(numeros)

numero_mas_grande = encontrar_numero_mas_grande(numeros)
print("\nNúmero más grande en la lista:", numero_mas_grande)