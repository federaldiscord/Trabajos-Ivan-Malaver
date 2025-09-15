import random

class Animal:
    def __init__(self, nombre, tipo, energia=100, posicion_x=0, posicion_y=0):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.vivo = True

    def mover(self):
        if self.vivo:
            self.posicion_x += random.randint(-1, 1)
            self.posicion_y += random.randint(-1, 1)
            self.energia -= 5
            if self.energia <= 0:
                self.vivo = False
                print(f"❌ {self.nombre} murió por falta de energía")

    def comer(self, otro):
        if not self.vivo:
            return
        if self.tipo == "carnívoro" and otro.vivo and otro.tipo == "herbívoro":
            if self.posicion_x == otro.posicion_x and self.posicion_y == otro.posicion_y:
                otro.vivo = False
                self.energia += 50
                print(f"🍖 {self.nombre} se comió a {otro.nombre} y recuperó energía")
        elif self.tipo == "herbívoro":
            if random.random() < 0.3:
                self.energia += 20
                print(f"🌿 {self.nombre} comió una planta y ganó energía")


animales = [
    Animal("Conejo1", "herbívoro"),
    Animal("Conejo2", "herbívoro"),
    Animal("Lobo1", "carnívoro"),
    Animal("Lobo2", "carnívoro")
]
print("ECOSISTEMA INICIAL")
for a in animales:
    print(f"{a.nombre} ({a.tipo}) → energía {a.energia}")
print("\n--- SIMULACIÓN ---")
for turno in range(1, 11):
    print(f"\nTurno {turno}")
    for animal in animales:
        animal.mover()
        if animal.tipo == "carnívoro":
            for presa in animales:
                if presa != animal:
                    animal.comer(presa)
        elif animal.tipo == "herbívoro":
            animal.comer(None)
    for a in animales:
        estado = "VIVO" if a.vivo else "MUERTO"
        print(f"{a.nombre} ({a.tipo}) → energía {a.energia}, pos=({a.posicion_x},{a.posicion_y}) [{estado}]")
