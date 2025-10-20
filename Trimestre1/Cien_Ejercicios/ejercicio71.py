import random

def generar_estudiantes(n):
    """Genera una lista de estudiantes con nombre y calificaciones."""
    nombres = ["Ana", "Luis", "María", "Pedro", "Sofía", "Carlos", "Lucía", "Jorge", "Elena", "Marta"]
    estudiantes = []
    for _ in range(n):
        nombre = random.choice(nombres)
        notas = tuple(random.randint(1, 10) for _ in range(3))  # tupla inmutable de 3 notas
        estudiante = {
            "nombre": nombre,
            "notas": notas,
            "promedio": round(sum(notas) / len(notas), 2)
        }
        estudiantes.append(estudiante)
    return estudiantes

def imprimir_estudiantes(lista):
    """Muestra estudiantes en formato tabla."""
    print(f"\n{'Nombre':<10} {'Notas':<15} {'Promedio':<8}")
    print("-"*35)
    for est in lista:
        print(f"{est['nombre']:<10} {est['notas']} {est['promedio']:<8}")
    print()


def ordenar_por_promedio(lista):
    """Ordena estudiantes usando inserción (de mayor a menor promedio)."""
    n = len(lista)
    for i in range(1, n):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["promedio"] < actual["promedio"]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = actual
    return lista


def buscar_binaria_nombre(lista, nombre):
    """Búsqueda binaria de estudiante por nombre (lista ordenada alfabéticamente)."""
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

estudiantes = generar_estudiantes(8)

print("🎓 Lista de estudiantes generada:")
imprimir_estudiantes(estudiantes)

ordenados_promedio = ordenar_por_promedio(estudiantes[:])
print("📊 Estudiantes ordenados por promedio:")
imprimir_estudiantes(ordenados_promedio)

ordenados_nombre = sorted(estudiantes, key=lambda e: e["nombre"])
nombre_buscar = "Ana"
indice = buscar_binaria_nombre(ordenados_nombre, nombre_buscar)

if indice != -1:
    print(f"✅ El estudiante '{nombre_buscar}' se encontró en el índice {indice}:")
    print(ordenados_nombre[indice])
else:
    print(f"❌ El estudiante '{nombre_buscar}' no está en la lista.")
