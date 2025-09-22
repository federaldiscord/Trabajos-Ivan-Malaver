def buscar_persona_por_nombre(personas, nombre):
    for persona in personas:
        if persona['nombre'] == nombre:
            return persona
    return None

personas = [
    {'nombre': 'Juan', 'edad': 25, 'genero': 'Masculino'},
    {'nombre': 'María', 'edad': 30, 'genero': 'Femenino'},
    {'nombre': 'Pedro', 'edad': 20, 'genero': 'Masculino'},
    {'nombre': 'Ana', 'edad': 35, 'genero': 'Femenino'}
]

nombre_persona = input("Ingrese el nombre de una persona: ")

persona_encontrada = buscar_persona_por_nombre(personas, nombre_persona)
if persona_encontrada:
    print("Persona encontrada:")
    print(persona_encontrada)
else:
    print("Persona no encontrada.")