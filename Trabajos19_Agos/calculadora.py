##Calculadora simple en Python

print("Ingresa los números y el operador para realizar la operación en el siguiente orden:")
print("Primer número, segundo número, y el signo operador.")

n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
operador = input("Operador (+, -, *, /): ")

if operador == "-":
    print("El resultado es:", n1 - n2)
elif operador == "+":
    print("El resultado es:", n1 + n2)
elif operador == "*":
    print("El resultado es:", n1 * n2)
elif operador == "/":
    if n2 != 0:
        print("El resultado es:", n1 / n2)
    else:
        print("Error, divisón por cero.")
else:
    print("Error, operador no válido.")
