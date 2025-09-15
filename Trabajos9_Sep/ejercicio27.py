def ordenamiento_burbuja(lista):
    n = len(lista)
    pasos = 0
    print(f"Lista inicial: {lista}")
    for i in range(n):
        for j in range(0, n - i - 1):
            pasos += 1
            print(f"Paso {pasos}: comparar {lista[j]} y {lista[j+1]}")
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(f"  Intercambio → {lista}")
    print(f"Lista final ordenada: {lista}")
    print(f"Total de pasos: {pasos}\n")
    return lista


def ordenamiento_quicksort(lista, profundidad=0):
    if len(lista) <= 1:
        return lista

    pivote = lista[len(lista) // 2]
    print(f"{'  '*profundidad}Dividir con pivote {pivote}: {lista}")

    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    return (ordenamiento_quicksort(menores, profundidad+1)
            + iguales
            + ordenamiento_quicksort(mayores, profundidad+1))


numeros = [34, 11, 55, 22, 77, 25, 44]

print("COMPARACIÓN DE ALGORITMOS DE ORDENAMIENTO")
print("=" * 50)
print("Lista original:", numeros)

print("\n1. ORDENAMIENTO BURBUJA:")
print("-" * 30)
ordenamiento_burbuja(numeros.copy())