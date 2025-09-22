import random

estudiantes = [
    ("Ana", [random.randint(60, 100) for _ in range(3)]),
    ("Luis", [random.randint(60, 100) for _ in range(3)]),
    ("María", [random.randint(60, 100) for _ in range(3)]),
    ("Pedro", [random.randint(60, 100) for _ in range(3)]),
    ("Sofía", [random.randint(60, 100) for _ in range(3)])
]

def promedio(notas):
    return sum(notas) / len(notas)

def ordenar_por_promedio(lista):
    return sorted(lista, key=lambda e: promedio(e[1]), reverse=True)

def buscar_estudiante(lista, nombre):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][0].lower() == nombre.lower():
            return medio
        elif lista[medio][0].lower() < nombre.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

print("Lista de estudiantes:")
for e in estudiantes:
    print(e[0], "Notas:", e[1], "Promedio:", promedio(e[1]))

print("\nEstudiantes ordenados por promedio:")
ordenados = ordenar_por_promedio(estudiantes)
for e in ordenados:
    print(e[0], promedio(e[1]))

print("\nBúsqueda de estudiante:")
estudiantes_ordenados_nombre = sorted(estudiantes, key=lambda e: e[0])
indice = buscar_estudiante(estudiantes_ordenados_nombre, "María")
if indice != -1:
    print("Encontrado:", estudiantes_ordenados_nombre[indice])
else:
    print("No encontrado")
