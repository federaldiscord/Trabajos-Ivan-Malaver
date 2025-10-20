import datetime

class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.id_libro}] {self.titulo} - {self.autor} ({estado})"


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre

    def __str__(self):
        return f"[{self.id_usuario}] {self.nombre}"


class Prestamo:
    def __init__(self, usuario, libro, dias=7):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.date.today()
        self.fecha_devolucion = self.fecha_prestamo + datetime.timedelta(days=dias)

    def __str__(self):
        return f"{self.usuario.nombre} tiene '{self.libro.titulo}' hasta {self.fecha_devolucion}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, titulo, autor):
        nuevo_id = len(self.libros) + 1
        libro = Libro(nuevo_id, titulo, autor)
        self.libros.append(libro)
        print(f"Libro registrado: {libro}")

    def registrar_usuario(self, nombre):
        nuevo_id = len(self.usuarios) + 1
        usuario = Usuario(nuevo_id, nombre)
        self.usuarios.append(usuario)
        print(f"Usuario registrado: {usuario}")

    def prestar_libro(self, id_usuario, id_libro):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = next((l for l in self.libros if l.id_libro == id_libro), None)

        if usuario and libro and libro.disponible:
            prestamo = Prestamo(usuario, libro)
            libro.disponible = False
            self.prestamos.append(prestamo)
            print(f"Préstamo exitoso: {prestamo}")
        else:
            print("No se pudo realizar el préstamo. Verifica usuario/libro.")

    def devolver_libro(self, id_libro):
        prestamo = next((p for p in self.prestamos if p.libro.id_libro == id_libro), None)
        if prestamo:
            prestamo.libro.disponible = True
            self.prestamos.remove(prestamo)
            print(f"Libro devuelto: {prestamo.libro.titulo}")
        else:
            print("El libro no está en préstamo.")

    def mostrar_libros(self):
        print("\nCatálogo de libros:")
        for libro in self.libros:
            print(libro)

    def mostrar_prestamos(self):
        print("\nPréstamos activos:")
        if not self.prestamos:
            print("No hay préstamos activos.")
        for prestamo in self.prestamos:
            print(prestamo)


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n===== GESTOR DE BIBLIOTECA =====")
        print("1. Registrar libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros")
        print("6. Mostrar préstamos")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            biblioteca.registrar_libro(titulo, autor)

        elif opcion == "2":
            nombre = input("Nombre del usuario: ")
            biblioteca.registrar_usuario(nombre)

        elif opcion == "3":
            id_usuario = int(input("ID de usuario: "))
            id_libro = int(input("ID de libro: "))
            biblioteca.prestar_libro(id_usuario, id_libro)

        elif opcion == "4":
            id_libro = int(input("ID de libro a devolver: "))
            biblioteca.devolver_libro(id_libro)

        elif opcion == "5":
            biblioteca.mostrar_libros()

        elif opcion == "6":
            biblioteca.mostrar_prestamos()

        elif opcion == "0":
            print("Saliendo del gestor de biblioteca...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()