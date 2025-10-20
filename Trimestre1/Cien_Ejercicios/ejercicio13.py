def encontrar_producto_primero(lista):
    producto = 1
    for numero in lista:
        if es_primo(numero):
            producto *= numero
    return producto

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros = [5, 2, 9, 1, 7, 4, 6, 3, 8]

print("Lista de números:")
print(numeros)

producto_numeros_primero = encontrar_producto_primero(numeros)
print("\nProducto de todos los números primos en la lista:", producto_numeros_primero)