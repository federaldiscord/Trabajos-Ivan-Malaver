def calcular_promedio_notas(estudiantes):
    notas_totales = 0
    cantidad_estudiantes = 0
    for estudiante in estudiantes:
        for nota in estudiante['notas']:
            notas_totales += nota
            cantidad_estudiantes += 1
    promedio = notas_totales / cantidad_estudiantes
    return promedio

estudiantes = [
    {'nombre': 'Juan', 'notas': [8, 7, 9]},
    {'nombre': 'María', 'notas': [6, 8, 7]},
    {'nombre': 'Pedro', 'notas': [9, 8, 7]}
]

promedio_notas = calcular_promedio_notas(estudiantes)
print("Promedio de notas de los estudiantes:", promedio_notas)