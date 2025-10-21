import random
humedad = 0
humedad = random.randint(0, 100)
print(f"La humedad actual es de: {humedad}% **recuerda que el rango aceptable de humedad es de 40% a 60%**")
if humedad < 0 or humedad > 100:
    print(f"El valor de humedad debe estar entre 0 y 100, el valor actual es de: {humedad}")
elif humedad < 40:
    print(f"La humedad está por debajo del rango aceptable, iniciando el proceso de riego, con un valor actual de: {humedad}%")
elif humedad > 60:
    print(f"La humedad supera el rango aceptable, deteniendo el proceso de riego, con un valor actual de: {humedad}%")
else:
    print(f"La humedad está dentro del rango aceptable, con un valor actual de: {humedad}%, no hay necesidad de iniciar ningún proceso")