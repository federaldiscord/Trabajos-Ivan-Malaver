# Sumador acumulativo
import time # Importamos la librería time para pausas
print("Sumando los números del 1 al 100...") # Indicamos que vamos
suma = 0 # Inicializamos la variable suma en 0
for i in range(1, 101): # Bucle que va del 1 al 100
    time.sleep(1) # Pausa de 1 segundo para ver el progreso
    suma += i # Sumamos el valor de i a la variable suma
    print(f"Suma hasta el momento {i}: {suma}") # Imprimimos la suma parcial
print("La suma de los números del 1 al 100 es:", suma) # Imprimimos el resultado
print("¡Hecho!") # Indicamos que hemos terminado