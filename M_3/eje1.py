def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b if b != 0 else "Error: división entre cero"

print("Operaciones: +  -  *  /")
op = input("Elige una operación: ")
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if op == '+':
    print("Resultado:", sumar(a, b))
elif op == '-':
    print("Resultado:", restar(a, b))
elif op == '*':
    print("Resultado:", multiplicar(a, b))
elif op == '/':
    print("Resultado:", dividir(a, b))
else:
    print("Operación no válida")