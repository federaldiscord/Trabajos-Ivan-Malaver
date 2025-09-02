def verif_Edad(edad):
    if edad >= 18:
        return "es mayor de edad"
    elif edad < 18:
        return "es menor de edad"

edad = int(input("Ingrese su edad: "))
if edad != int(edad) or edad < 0:
    print("Edad no valida")

print(verif_Edad(edad))