import math

def calcular_area(figura, **kwargs):
    if figura == "rectangulo":
        base = kwargs["base"]
        altura = kwargs["altura"]
        area = base * altura
    elif figura == "triangulo":
        base = kwargs["base"]
        altura = kwargs["altura"]
        area = (base * altura) / 2
    elif figura == "circulo":
        radio = kwargs["radio"]
        area = math.pi * radio ** 2
    else:
        area = 0

    return area

figura = input("Ingrese el tipo de figura (rectangulo, triangulo o circulo): ")
if figura == "rectangulo" or figura == "triangulo":
    base = float(input("Ingrese la base de la figura: "))
    altura = float(input("Ingrese la altura de la figura: "))
elif figura == "circulo":
    radio = float(input("Ingrese el radio de la figura: "))
else:
    print("Tipo de figura inválido")
    exit()

area = calcular_area(figura, base=base, altura=altura, radio=radio)
print("Área de la figura:", area)