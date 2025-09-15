print("La siguiente calculadora te servirá para hacer la conversión de Celsius a Fahrenheit.") # Explicación del programa
print("Ingresa la cantidad de grados a convertir.") # Indicamos al usuario qué hacer
grados = float(input("Grados Celsius: ")) # Solicitamos los grados a convertir
fahrenheit = grados * 9/5 + 32 # Realizamos la conversión
print(f"La conversión arroja un total de: {fahrenheit}°F") # Imprimimos el resultado