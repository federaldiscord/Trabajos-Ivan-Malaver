import math
def calcular_area(figura, base, altura):
    if figura == "rectangulo":
        area = base * altura
    elif figura == "triangulo":
        area = (base * altura) / 2
    elif figura == "circulo":
        area = math.pi * (base / 2) ** 2
    else:
        area = 0

    return area

figura = input("Ingrese el tipo de figura (rectangulo, triangulo o circulo): ")
if figura == "rectangulo" or figura == "triangulo":
    base = float(input("Ingrese la base de la figura: "))
    altura = float(input("Ingrese la altura de la figura: "))
elif figura == "circulo":
    base = float(input("Ingrese el diámetro de la figura: "))
else:
    print("Tipo de figura inválido")
    exit()

area = calcular_area(figura, base, altura)
print("Área de la figura:", area)