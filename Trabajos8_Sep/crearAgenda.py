# Setup de la agenda
'''archivo = open("agenda.txt", "w", encoding="utf-8")''' # Línea de código para crear el archivo

print("Manual de usuario: \nPodrás ingresar nombres y teléfonos, ver la agenda o salir.") #instrucción de uso

def agregar_contacto():
    with open("agenda.txt", "a", encoding="utf-8") as archivo:
        nombre = str(input("Nombre: ")) # Solicita el nombre del contacto
        if nombre.strip() == "":
            print("El nombre no puede estar vacío.")
            return
        telefono = input("Teléfono: ")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Teléfono: {telefono}\n")
        print("Contacto agregado correctamente.")

def ver_agenda():
    try:
        with open("agenda.txt", "r", encoding="utf-8") as archivo:
            print("\n--- Agenda ---")
            print(archivo.read())
    except FileNotFoundError:
        print("La agenda está vacía o no existe.")

def inicializar_agenda():
    try:
        with open("agenda.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if "Agenda" not in contenido:
                raise FileNotFoundError
    except FileNotFoundError:
        with open("agenda.txt", "w", encoding="utf-8") as archivo:
            archivo.write("Agenda\n") # Título de la agenda
            archivo.write("===================\n") # Línea divisoria

inicializar_agenda()

while True:
    print("\nMenú:")
    print("1. Agregar contacto")
    print("2. Ver agenda")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        ver_agenda()
    elif opcion == "3":
        with open("agenda.txt", "a", encoding="utf-8") as archivo:
            archivo.write("===================\n") # Línea divisoria final
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")