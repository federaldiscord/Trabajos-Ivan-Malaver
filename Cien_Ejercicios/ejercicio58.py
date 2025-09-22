import math

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        estado_nutricional = "Peso inferior al normal"
    elif imc >= 18.5 and imc < 25:
        estado_nutricional = "Peso normal"
    elif imc >= 25 and imc < 30:
        estado_nutricional = "Sobrepeso"
    elif imc >= 30 and imc < 35:
        estado_nutricional = "Obesidad grado I"
    elif imc >= 35 and imc < 40:
        estado_nutricional = "Obesidad grado II"
    elif imc >= 40:
        estado_nutricional = "Obesidad grado III"
    return imc, estado_nutricional

nombre = input("Ingrese el nombre de la persona: ")
peso = float(input("Ingrese el peso de la persona en kg: "))
altura = float(input("Ingrese la altura de la persona en metros: "))

imc, estado_nutricional = calcular_imc(peso, altura)

print("IMC de", nombre, ":", imc)
print("Estado nutricional:", estado_nutricional)