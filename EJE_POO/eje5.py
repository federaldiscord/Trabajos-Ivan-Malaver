class Estudiante:
    """Clase que representa a un estudiante con calificaciones."""

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones: list[float] = []

    def agregar_calificacion(self, nota: float) -> None:
        if not (0 <= nota <= 10):
            raise ValueError("La calificación debe estar entre 0 y 10.")
        self.calificaciones.append(nota)

    def calcular_promedio(self) -> float:
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self) -> str:
        promedio = self.calcular_promedio()
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Promedio: {promedio:.2f}"


if __name__ == "__main__":
    est = Estudiante("María", 20)
    est.agregar_calificacion(9.5)
    est.agregar_calificacion(8.0)
    est.agregar_calificacion(10.0)
    print(est)
