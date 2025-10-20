contraseña = str(input("Por favor ingrese su contraseña: ")) # Solicitamos la contraseña al usuario
if len(contraseña) < 8: # Verificamos si la longitud de la contraseña es menor a 8
    print("Contraseña inválida, debe tener al menos 8 caracteres.") # Imprimimos que la contraseña es inválida
else: # Si la longitud es 8 o mayor
    print("Contraseña válida.") # Imprimimos que la contraseña es válida
    print(f"longitud de la contraseña: {len(contraseña)}") # Imprimimos la longitud de la contraseña

    if len(contraseña) >= 12: # Verificamos si la longitud de la contraseña es 12 o mayor
        print("Contraseña robusta.") # Imprimimos que la contraseña es robusta
        if contraseña.islower(): 
            print("La contraseña debe incluir al menos una letra mayúscula.")
        if contraseña.isalpha():
            print("La contraseña debe incluir al menos un número o un carácter especial.")
        if contraseña.isalnum():
            print("La contraseña debe incluir al menos un carácter especial.")