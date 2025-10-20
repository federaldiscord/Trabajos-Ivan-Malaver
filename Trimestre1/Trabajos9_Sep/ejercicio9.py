import random
import time

numero_secreto = random.randint(1, 100) # Generamos un número aleatorio entre 1 y 100
intentos = 0 # Contador de intentos
print("¡Vas a adivinar el número que estoy pensando!") # Mensaje de bienvenida
time.sleep(2) # Pausa de 2 segundos
print("Estoy pensando en un número entre 1 y 100.") # Indicamos el rango
while True: # Bucle infinito hasta que el usuario adivine el número
    intento = int(input("Ingresa tu intento: ")) # Solicitamos un intento al usuario
    intentos += 1 # Incrementamos el contador de intentos
    if intento < numero_secreto: # Si el intento es menor al número secreto
        print("Demasiado bajo. Intenta de nuevo.") # Indicamos que es demasiado bajo
    elif intento > numero_secreto: # Si el intento es mayor al número secreto
        print("Demasiado alto. Intenta de nuevo.") # Indicamos que es demasiado alto
    else: # Si el intento es igual al número secreto
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.") # Felicitamos al usuario
        break # Salimos del bucle