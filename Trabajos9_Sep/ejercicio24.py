# Generador de contraseñas
import random # Importamos la librería random para generar números aleatorios
import string # Importamos la librería string para usar caracteres predefinidos

while True:
    longitud = int(input("Ingrese la longitud deseada para la contraseña (mínimo 8 caracteres): ")) # Pedimos al usuario ingresar la longitud de la contraseña
    if longitud < 8: # Verificamos si la longitud es menor a 8
        print("La longitud debe ser al menos 8 caracteres.") # Imprimimos que la longitud es inválida
    else: # Si la longitud es 8 o mayor
        caracteres = string.ascii_letters + string.digits + string.punctuation # Definimos los caracteres que se pueden usar en la contraseña (letras, números y símbolos)
        contraseña = "".join(random.choice(caracteres) for _ in range(longitud)) # Generamos la contraseña seleccionando caracteres aleatorios
        print(f"Tu contraseña generada es: {contraseña}") # Imprimimos la contraseña generada
        if longitud >= 12: # Verificamos si la longitud es 12 o mayor
            print("Contraseña robusta.") # Imprimimos que la contraseña es robusta
            if contraseña.islower(): 
                print("La contraseña debe incluir al menos una letra mayúscula.")
            if contraseña.isalpha():
                print("La contraseña debe incluir al menos un número o un carácter especial.")
            if contraseña.isalnum():
                print("La contraseña debe incluir al menos un carácter especial.")
        break