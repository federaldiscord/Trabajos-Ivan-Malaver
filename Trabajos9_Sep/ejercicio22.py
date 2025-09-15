# Calculadora con funciones
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

input1 = float(input("Ingrese el primer número a operar: "))
input2 = float(input("Ingrese el segundo número a operar: "))

print(f"Suma: {sumar(input1, input2)}")
print(f"Resta: {restar(input1, input2)}")
print(f"Multiplicación: {multiplicar(input1, input2)}")
print(f"División: {dividir(input1, input2)}")