class Rectangulo:
    """Clase que representa un rectángulo con métodos geométricos básicos."""

    def __init__(self, ancho: float, alto: float):
        if ancho <= 0 or alto <= 0:
            raise ValueError("El ancho y el alto deben ser valores positivos.")
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self) -> float:
        return self.ancho * self.alto

    def calcular_perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)

    def es_cuadrado(self) -> bool:
        return self.ancho == self.alto

    def __str__(self) -> str:
        tipo = "cuadrado" if self.es_cuadrado() else "rectángulo"
        return (f"{tipo.capitalize()} - Ancho: {self.ancho}, Alto: {self.alto}, "
                f"Área: {self.calcular_area()}, Perímetro: {self.calcular_perimetro()}")


if __name__ == "__main__":
    rect = Rectangulo(5, 5)
    print(rect)
    otro = Rectangulo(4, 6)
    print(otro)
