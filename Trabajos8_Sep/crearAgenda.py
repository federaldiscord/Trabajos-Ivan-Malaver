# Setup de la agenda
'''archivo = open("agenda.txt", "w", encoding="utf-8")''' # Línea de código para crear el archivo

print("Manual de usuaio: \nPodrás ingresar nombres y teléfonos hasta que decidas salir (ingresando 'salir' como nombre)") #instrucción de uso
with open("agenda.txt", "a", encoding="utf-8") as archivo: # Abre el archivo en modo de adición
    archivo.write("Agenda\n") # Título de la agenda
    archivo.write("===================\n") # Línea divisoria
    while True: # Bucle para ingresar múltiples contactos
        nombre = str(input("Nombre: ")) # Solicita el nombre del contacto
        if nombre.lower() == 'salir': # Condición para salir del bucle
            break # Sale del bucle si el usuario ingresa 'salir'
        archivo.write("Nombre: " + nombre + "\n") # Escribe el nombre en el archivo
        archivo.write("Teléfono: " + input("Teléfono: ") + "\n") # Solicita y escribe el teléfono en el archivo
    archivo.write("===================\n") # Línea divisoria final