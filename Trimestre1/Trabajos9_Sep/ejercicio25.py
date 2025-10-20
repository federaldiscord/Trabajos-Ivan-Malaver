# Sistema de registro de estudiantes

estudiantes = []
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    grado = input("Ingrese el grado del estudiante: ")
    estudiantes.append({"nombre": nombre, "edad": edad , "grado": grado})
    print(f"Estudiante {nombre} registrado correctamente.")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("\nLista de estudiantes registrados:")
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"{i}. Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Grado: {estudiante['grado']}")

def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    encontrados = [e for e in estudiantes if e['nombre'].lower() == nombre.lower()]
    if encontrados:
        for estudiante in encontrados:
            print(f"Estudiante encontrado: Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Grado: {estudiante['grado']}")
    else:
        print("No se encontró ningún estudiante con ese nombre.")

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    global estudiantes
    estudiantes = [e for e in estudiantes if e['nombre'].lower() != nombre.lower()]
    print(f"Estudiante {nombre} eliminado si existía.")

while True:
    print("\nMenú:")
    print("1. Registrar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")
    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        buscar_estudiante()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")