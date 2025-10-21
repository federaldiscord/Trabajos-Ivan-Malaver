class ContadorTexto:
    """Clase para contar palabras, caracteres y líneas de un texto."""

    def __init__(self, texto: str):
        self.texto = texto.strip()

    def contar_palabras(self) -> int:
        palabras = [p for p in self.texto.split() if p]
        return len(palabras)

    def contar_caracteres(self) -> int:
        return len(self.texto)

    def contar_lineas(self) -> int:
        if not self.texto:
            return 0
        return self.texto.count("\n") + 1

    def __str__(self) -> str:
        return (
            f"Palabras: {self.contar_palabras()}, "
            f"Caracteres: {self.contar_caracteres()}, "
            f"Líneas: {self.contar_lineas()}"
        )


if __name__ == "__main__":
    texto = """Hola mundo.
Este es un ejemplo de texto.
Contaremos palabras, líneas y caracteres."""
    contador = ContadorTexto(texto)
    print(contador)
