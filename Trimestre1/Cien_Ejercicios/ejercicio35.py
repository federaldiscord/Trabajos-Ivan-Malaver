def calcular_promedio_notas(notas):
    suma_notas = sum(notas)
    cantidad_notas = len(notas)
    promedio = suma_notas / cantidad_notas
    return promedio

notas = []
cantidad_notas = int(input("Ingrese la cantidad de notas: "))
for i in range(cantidad_notas):
    nota = float(input("Ingrese la nota", i+1, ": "))
    notas.append(nota)

promedio = calcular_promedio_notas(notas)
print("Promedio de notas:", promedio)

if promedio >= 4:
    print("El estudiante aprueba")
else:
    print("El estudiante reprueba")

materias = ["Matemáticas", "Español", "Inglés", "Historia", "Ciencias"]
for i, materia in enumerate(materias):
    if notas[i] >= 4:
        print(materia, "aprobado")
    else:
        print(materia, "reprobado")