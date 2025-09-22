def calcular_promedio_edad(personas):
    personas_mayores = [persona for persona in personas if persona['edad'] >= 18]
    promedio = sum(persona['edad'] for persona in personas_mayores) / len(personas_mayores)
    return promedio

personas = [
    {'nombre': 'Juan', 'edad': 25, 'genero': 'Masculino'},
    {'nombre': 'María', 'edad': 30, 'genero': 'Femenino'},
    {'nombre': 'Pedro', 'edad': 20, 'genero': 'Masculino'},
    {'nombre': 'Ana', 'edad': 35, 'genero': 'Femenino'}
]

print("Lista de personas:")
for persona in personas:
    print(persona)

promedio_edad = calcular_promedio_edad(personas)
print("\nPromedio de edad de las personas mayores de 18 años:", promedio_edad)