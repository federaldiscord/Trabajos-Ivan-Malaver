edad = int(input("Por favor ingrese su edad: ")) # Pedimos al usuario ingresar su edad
if edad < 18: # Verificamos si la edad es menor a 18
    print("Eres menor de edad.") # Imprimimos que es menor de edad
elif edad == 18: # Verificamos si la edad es igual a 18
    print("Tienes 18 años, eres mayor de edad.") # Imprimimos que tiene 18 años y es mayor de edad
else: # Si no se cumple ninguna de las condiciones anteriores
    print("Eres mayor de edad.") # Imprimimos que es mayor de edad