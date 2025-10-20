def ordenar_por_edad(personas):
    personas_ordenadas = sorted(personas, key=lambda persona: persona['edad'])
    return personas_ordenadas

juan = {'nombre': 'Juan', 'edad': 25, 'genero': 'Masculino'}
maria = {'nombre': 'María', 'edad': 30, 'genero': 'Femenino'}
pedro = {'nombre': 'Pedro', 'edad': 20, 'genero': 'Masculino'}
ana = {'nombre': 'Ana', 'edad': 35, 'genero': 'Femenino'}

personas = [juan, maria, pedro, ana]

print("Lista de personas sin ordenar:")
print(juan)
print(maria)
print(pedro)
print(ana)

personas_ordenadas = ordenar_por_edad(personas)
print("\nLista de personas ordenada por edad:")
for persona in personas_ordenadas:
    print(persona)