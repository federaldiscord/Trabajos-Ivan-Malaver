import math

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

nombre = input("Ingrese el nombre de la persona: ")
peso = float(input("Ingrese el peso de la persona: "))
altura = float(input("Ingrese la altura de la persona en metros: "))

imc = calcular_imc(peso, altura)
print("IMC de", nombre, ":", imc)

if imc < 18.5:
    print(nombre, "está por debajo del peso ideal")
elif imc >= 18.5 and imc < 25:
    print(nombre, "tiene un peso ideal")
elif imc >= 25 and imc < 30:
    print(nombre, "tiene sobrepeso")
elif imc >= 30 and imc < 35:
    print(nombre, "tiene obesidad grado I")
elif imc >= 35 and imc < 40:
    print(nombre, "tiene obesidad grado II")
elif imc >= 40:
    print(nombre, "tiene obesidad grado III")