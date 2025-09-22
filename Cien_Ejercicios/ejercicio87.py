import random

empleados = [
    {"nombre": "Ana", "puesto": "Gerente", "salario": random.randint(3000, 6000)},
    {"nombre": "Luis", "puesto": "Analista", "salario": random.randint(2000, 4000)},
    {"nombre": "María", "puesto": "Programador", "salario": random.randint(1500, 3500)},
    {"nombre": "Pedro", "puesto": "Diseñador", "salario": random.randint(1800, 3200)},
    {"nombre": "Sofía", "puesto": "Soporte", "salario": random.randint(1200, 2500)}
]

def ordenar_por_salario(lista):
    return sorted(lista, key=lambda e: e["salario"], reverse=True)

def buscar_empleado(lista, nombre):
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

print("Lista de empleados:")
for e in empleados:
    print(e["nombre"], "-", e["puesto"], "-", e["salario"], "USD")

print("\nEmpleados ordenados por salario:")
ordenados = ordenar_por_salario(empleados)
for e in ordenados:
    print(e["nombre"], e["salario"])

print("\nBúsqueda de empleado:")
empleados_ordenados_nombre = sorted(empleados, key=lambda e: e["nombre"])
indice = buscar_empleado(empleados_ordenados_nombre, "María")
if indice != -1:
    print("Encontrado:", empleados_ordenados_nombre[indice])
else:
    print("No encontrado")
