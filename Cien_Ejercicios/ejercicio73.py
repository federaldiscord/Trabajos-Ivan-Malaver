empleados = [
    {"nombre": "Ana", "departamento": "Ventas", "salario": (1200, 200)},
    {"nombre": "Luis", "departamento": "IT", "salario": (1500, 300)},
    {"nombre": "Marta", "departamento": "Marketing", "salario": (1100, 150)},
    {"nombre": "Pedro", "departamento": "Ventas", "salario": (1300, 250)},
    {"nombre": "Sofía", "departamento": "IT", "salario": (1600, 400)},
]

def calcular_salario_total(empleado):
    """Calcula el salario total de un empleado (base + bonificación)."""
    base, bono = empleado["salario"]
    return base + bono


def imprimir_empleados(lista):
    """Muestra empleados en formato tabla."""
    print(f"\n{'Nombre':<10} {'Departamento':<15} {'Base':<8} {'Bono':<6} {'Total':<8}")
    print("-"*60)
    for emp in lista:
        base, bono = emp["salario"]
        print(f"{emp['nombre']:<10} {emp['departamento']:<15} {base:<8} {bono:<6} {calcular_salario_total(emp):<8}")
    print()


def ordenar_por_salario(lista):
    """Ordena empleados por salario total (burbuja)."""
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if calcular_salario_total(lista[j]) > calcular_salario_total(lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


def buscar_binaria_nombre(lista, nombre):
    """Búsqueda binaria por nombre (lista ordenada alfabéticamente)."""
    inicio, final = 0, len(lista) - 1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio]["nombre"].lower() == nombre.lower():
            return medio
        elif lista[medio]["nombre"].lower() < nombre.lower():
            inicio = medio + 1
        else:
            final = medio - 1
    return -1

print("👨‍💼 Lista de empleados:")
imprimir_empleados(empleados)

empleados_ordenados_salario = ordenar_por_salario(empleados[:])
print("💰 Empleados ordenados por salario total:")
imprimir_empleados(empleados_ordenados_salario)

empleados_ordenados_nombre = sorted(empleados, key=lambda e: e["nombre"])
nombre_buscar = "Sofía"
indice = buscar_binaria_nombre(empleados_ordenados_nombre, nombre_buscar)

if indice != -1:
    print(f"✅ El empleado '{nombre_buscar}' se encontró en el índice {indice}:")
    print(empleados_ordenados_nombre[indice])
else:
    print(f"❌ El empleado '{nombre_buscar}' no está en la empresa.")
