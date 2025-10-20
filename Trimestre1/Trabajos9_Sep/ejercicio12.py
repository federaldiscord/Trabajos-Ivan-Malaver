# Tabla de multiplicar del 1 al 10 según escoja el usuario
numero = int(input("Ingrese un número para ver la tabla de multiplicar ")) # Pedimos al usuario ingresar un número
print(f"Tabla de multiplicar del {numero}:") # Indicamos de qué número es la tabla
for i in range(1, 11): # Bucle que va del 1 al 10
    resultado = numero * i # Calculamos el resultado de la multiplicación
    print(f"{numero} x {i} = {resultado}") # Imprimimos el resultado de la multiplicación