def verif_Edad(edad):
    if edad >= 18:
        return "es mayor de edad"
    elif edad < 0:
        return "es menor de edad"

edad = int(input("Ingrese su edad: "))

print(verif_Edad(edad))