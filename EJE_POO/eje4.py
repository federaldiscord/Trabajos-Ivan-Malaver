class Tarea:
    """Representa una tarea individual."""
    def __init__(self, descripcion: str):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self) -> None:
        self.completada = True

    def __str__(self) -> str:
        estado = "✅" if self.completada else "❌"
        return f"{estado} {self.descripcion}"


class ListaTareas:
    """Maneja una colección de tareas."""
    def __init__(self):
        self.__tareas: list[Tarea] = []

    def agregar_tarea(self, descripcion: str) -> None:
        self.__tareas.append(Tarea(descripcion))

    def eliminar_tarea(self, indice: int) -> None:
        if indice < 0 or indice >= len(self.__tareas):
            raise IndexError("Índice fuera de rango.")
        self.__tareas.pop(indice)

    def marcar_completada(self, indice: int) -> None:
        if indice < 0 or indice >= len(self.__tareas):
            raise IndexError("Índice fuera de rango.")
        self.__tareas[indice].marcar_completada()

    def mostrar_tareas(self) -> None:
        if not self.__tareas:
            print("No hay tareas en la lista.")
            return
        for i, tarea in enumerate(self.__tareas):
            print(f"{i + 1}. {tarea}")


if __name__ == "__main__":
    lista = ListaTareas()
    lista.agregar_tarea("Estudiar Python")
    lista.agregar_tarea("Hacer ejercicio")
    lista.mostrar_tareas()
    lista.marcar_completada(0)
    print("\nDespués de completar la primera tarea:")
    lista.mostrar_tareas()
