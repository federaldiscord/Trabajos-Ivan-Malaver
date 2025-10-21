class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f"Me llamo {self.nombre} y soy un {self.especie} de {self.edad} años")

mascota1 = Mascota("Fido", "Perro", 5)
mascota2 = Mascota("Luna", "Gato", 3)
mascota3 = Mascota("Leo", "Tigre", 8)
