def calcular_potencia(base, exponente):
    resultado = base ** exponente
    return resultado

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

potencia = calcular_potencia(base, exponente)
print("Potencia de", base, "a la", exponente, ":", potencia)