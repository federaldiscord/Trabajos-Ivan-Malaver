class Calculadora:
    """Clase Calculadora con operaciones básicas."""

    def sumar(self, a: float, b: float) -> float:
        return a + b

    def restar(self, a: float, b: float) -> float:
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        return a * b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b


if __name__ == "__main__":
    calc = Calculadora()
    print("Suma:", calc.sumar(5, 3))
    print("Resta:", calc.restar(5, 3))
    print("Multiplicación:", calc.multiplicar(5, 3))
    print("División:", calc.dividir(5, 3))
