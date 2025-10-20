# Contador del 1 al 10
import time # Importamos la librería time para pausas
print("Contando del 1 al 10...") # Indicamos que vamos a contar
print("Pensando...")
time.sleep(2) # Pausa de 2 segundos

for i in range(1, 11): # Bucle que va del 1 al 10
    time.sleep(1) # Pausa de 1 segundos
    print(i) # Imprimimos el número actual
print("¡Hecho!") # Indicamos que hemos terminado