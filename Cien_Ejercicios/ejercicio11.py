import random

def generar_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            numero = random.randint(1, 10)
            fila.append(numero)
        matriz.append(fila)
    return matriz

n = int(input("Ingrese el tamaño de la matriz (n x n): "))

matriz = generar_matriz(n)
print("Matriz generada:")
for fila in matriz:
    print(fila)

def encontrar_suma_fila(matriz, fila):
    suma = 0
    for elemento in matriz[fila]:
        suma += elemento
    return suma

fila = int(input("Ingrese el número de fila para encontrar la suma: "))

suma_fila = encontrar_suma_fila(matriz, fila)
print("Suma de los elementos de la fila", fila, ":", suma_fila)