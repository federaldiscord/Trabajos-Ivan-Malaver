import random

autos = [
    {"marca": "Ferrari", "modelo": "488", "velocidad_max": random.randint(280, 340)},
    {"marca": "Lamborghini", "modelo": "Huracán", "velocidad_max": random.randint(290, 350)},
    {"marca": "Porsche", "modelo": "911", "velocidad_max": random.randint(270, 330)},
    {"marca": "Bugatti", "modelo": "Chiron", "velocidad_max": random.randint(400, 450)},
    {"marca": "McLaren", "modelo": "720S", "velocidad_max": random.randint(300, 350)}
]

def ordenar_por_velocidad(lista):
    return sorted(lista, key=lambda a: a["velocidad_max"], reverse=True)

def buscar_auto(lista, modelo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio]["modelo"].lower() == modelo.lower():
            return medio
        elif lista[medio]["modelo"].lower() < modelo.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

print("Lista de autos:")
for a in autos:
    print(a["marca"], a["modelo"], "-", a["velocidad_max"], "km/h")

print("\nAutos ordenados por velocidad máxima:")
ordenados = ordenar_por_velocidad(autos)
for a in ordenados:
    print(a["marca"], a["modelo"], "-", a["velocidad_max"], "km/h")

print("\nBúsqueda de auto por modelo:")
autos_ordenados_modelo = sorted(autos, key=lambda a: a["modelo"])
indice = buscar_auto(autos_ordenados_modelo, "911")
if indice != -1:
    print("Encontrado:", autos_ordenados_modelo[indice])
else:
    print("No encontrado")
