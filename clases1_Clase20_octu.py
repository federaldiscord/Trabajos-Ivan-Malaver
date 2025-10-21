class vehiculo:
    def __init__(self, color, marca, motor):
        self.color=color
        self.marca=marca
        self.motor=motor

    def mostrarInfo(self):
        return(f"el coche es de color {self.color}, tiene una marca {self.marca}, y un motor {self.motor}")
vehiculo1 = vehiculo("negro", "Toyota", "V4")
print(vehiculo1.mostrarInfo())


class figura:
    def area(self):
        self.base=2
        self.altura=3

mi_figura=figura()
mi_figura.area()

el_area=(mi_figura.base * mi_figura.altura)
print(f"el area de la figura es: {el_area}")