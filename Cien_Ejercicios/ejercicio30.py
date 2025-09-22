import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio)
print("Área del círculo:", area)