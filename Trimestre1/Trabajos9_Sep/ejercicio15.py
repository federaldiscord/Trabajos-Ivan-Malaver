# Jueg de adivinanza con límite de intentos
import random
import time
numero_secreto = random.randint(1, 100) # Generamos un número aleatorio entre 1 y 100
intentos = 0 # Contador de intentos
max_intentos = 10 # Definimos el número máximo de intentos
print("¡Vas a adivinar el número que estoy pensando!") # Mensaje de bienvenida
time.sleep(2) # Pausa de 2 segundos
print("Estoy pensando en un número entre 1 y 100. Tienes 10 intentos.") # Indicamos el rango y los intentos
while intentos < max_intentos: # Bucle hasta que se alcancen los intentos máximos
    intento = int(input("Ingresa tu número: ")) # Solicitamos un intento al usuario
    intentos += 1 # Incrementamos el contador de intentos
    if intento < numero_secreto: # Si el intento es menor al número secreto
        print("Demasiado bajo. Intenta de nuevo.") # Indicamos que es demasiado bajo
    elif intento > numero_secreto: # Si el intento es mayor al número secreto
        print("Demasiado alto. Intenta de nuevo.") # Indicamos que es demasiado alto
    else: # Si el intento es igual al número secreto
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.") # Felicitamos al usuario
        break # Salimos del bucle
else: # Si se alcanzan los intentos máximos sin adivinar
    print(f"Lo siento, has agotado tus {max_intentos} intentos. El número era {numero_secreto}.") # Informamos al usuario del número correcto
print("¡Gracias por jugar!") # Agradecemos al usuario por jugar