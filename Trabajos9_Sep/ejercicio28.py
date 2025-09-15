def contar_frecuencias(lista):
    frecuencias = {}
    print(f"Analizando lista: {lista}")
    print("\nProceso de conteo:")
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
            print(f"  {elemento}: incrementado a {frecuencias[elemento]}")
        else:
            frecuencias[elemento] = 1
            print(f"  {elemento}: primera aparición")
    return frecuencias


def encontrar_mas_frecuente(frecuencias):
    if not frecuencias:
        return None, 0
    elemento_max = max(frecuencias, key=frecuencias.get)
    frecuencia_max = frecuencias[elemento_max]
    return elemento_max, frecuencia_max


def mostrar_estadisticas(frecuencias):
    print("\n" + "=" * 40)
    print("ESTADÍSTICAS DE FRECUENCIA")
    print("=" * 40)

    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

    total_elementos = sum(frecuencias.values())
    elementos_unicos = len(frecuencias)
    print(f"Total de elementos: {total_elementos}")
    print(f"Elementos únicos: {elementos_unicos}")

    print("\nFrecuencias (ordenadas por cantidad):")
    for elemento, frecuencia in frecuencias_ordenadas:
        porcentaje = (frecuencia / total_elementos) * 100
        barra = "-" * frecuencia
        print(f"  {elemento:>3}: {frecuencia:>2} veces ({porcentaje:4.1f}%) {barra}")

    mas_frecuente, max_freq = encontrar_mas_frecuente(frecuencias)
    print(f"\nElemento más frecuente: {mas_frecuente} ({max_freq} veces)")


print("CONTADOR DE FRECUENCIAS")
print("=" * 30)

numeros = [1, 2, 3, 2, 1, 4, 2, 5, 2, 1, 3, 2]
frecuencias_num = contar_frecuencias(numeros)
mostrar_estadisticas(frecuencias_num)

print("\n" + "=" * 50)
texto = "programacion"
letras = list(texto)
print(f"\nAnalizando la palabra: '{texto}'")
frecuencias_letras = contar_frecuencias(letras)
mostrar_estadisticas(frecuencias_letras)