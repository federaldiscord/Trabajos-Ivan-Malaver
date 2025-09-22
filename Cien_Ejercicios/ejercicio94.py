import random

instrumentos = [
    {"nombre": "Guitarra", "precio": 350},
    {"nombre": "Piano", "precio": 1200},
    {"nombre": "Batería", "precio": 800},
    {"nombre": "Violín", "precio": 500},
    {"nombre": "Flauta", "precio": 150}
]

def ordenar_por_precio(lista):
    return sorted(lista, key=lambda x: x["precio"])

def buscar_instrumento(lista, nombre):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio]["nombre"].lower() == nombre.lower():
            return medio
        elif lista[medio]["nombre"].lower() < nombre.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

print("Lista de instrumentos:")
for i in instrumentos:
    print(i["nombre"], "- $", i["precio"])

print("\nInstrumentos ordenados por precio:")
ordenados = ordenar_por_precio(instrumentos)
for i in ordenados:
    print(i["nombre"], "- $", i["precio"])

print("\nBúsqueda de instrumento:")
instrumentos_ordenados_nombre = sorted(instrumentos, key=lambda x: x["nombre"])
indice = buscar_instrumento(instrumentos_ordenados_nombre, "Violín")
if indice != -1:
    print("Encontrado:", instrumentos_ordenados_nombre[indice])
else:
    print("No encontrado")
