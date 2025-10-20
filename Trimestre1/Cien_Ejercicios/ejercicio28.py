def calcular_perimetro(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    return perimetro

lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    perimetro = calcular_perimetro(lado1, lado2, lado3)
    print("Perímetro del triángulo:", perimetro)
else:
    print("Los lados ingresados no forman un triángulo válido")