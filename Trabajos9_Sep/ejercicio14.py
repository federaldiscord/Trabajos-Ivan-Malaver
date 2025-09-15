import time # Importamos la librería time para pausas
print("Detector de números pares") # Indicamos el propósito del programa

# Detector de números pares
num = int(input("Por favor ingrese un número: ")) # Pedimos al usuario ingresar un número
print("Pensando...") # Indicamos que estamos procesando
time.sleep(1) # Pausa de 1 segundo para mejor experiencia
if num % 2 == 0: # Verificamos si el número es par
    print(f"El número {num} es par.") # Imprimimos que el número es par
else: # Si el número no es par
    print(f"El número {num} es impar.") # Imprimimos que el número es impar