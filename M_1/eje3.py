datos = input("Ingrese números separados por espacio: ").split()
numeros = [float(n) for n in datos]

print(f"Promedio: {sum(numeros)/len(numeros):.2f}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")