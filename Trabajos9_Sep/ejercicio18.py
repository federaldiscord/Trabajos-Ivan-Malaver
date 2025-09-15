# Calculadora de calificaciones
notas = [] # Lista para almacenar las notas
for i in range(5): # Bucle para pedir 5 notas
    nota = float(input(f"Ingrese la nota {i+1} (0 - 5): ")) # Pedimos al usuario ingresar una nota
    while nota < 0 or nota > 5: # Verificamos que la nota esté entre 0 y 5
        print("Nota inválida. Por favor ingrese una nota entre 0 y 5.")
        nota = float(input(f"Ingrese la nota {i+1} (0 - 5): ")) # Pedimos nuevamente la nota si es inválida
    notas.append(nota) # Agregamos la nota a la lista
promedio = sum(notas) / len(notas) # Calculamos el promedio de las notas
print(f"El promedio de las notas es: {promedio:.2f}") # Imprimimos el promedio con 2 decimales
if promedio >= 3.5: # Verificamos si el promedio es mayor o igual a 3.5
    print("¡Aprobado!") # Imprimimos que aprobó
else: # Si el promedio es menor a 3.5
    print("No aprobado") # Imprimimos que no aprobó

# Estadísticas de las notas
print(f"La nota más alta es: {max(notas)}") # Imprimimos la nota más alta
print(f"La nota más baja es: {min(notas)}") # Imprimimos la nota más baja
print(f"La cantidad de notas ingresadas es: {len(notas)}") # Imprimimos la cantidad de notas ingresadas
print("Las notas ingresadas son:", notas) # Imprimimos la lista de notas ingresadas ordenadas
notas.sort() # Ordenamos la lista de notas
print("Las notas ingresadas ordenadas son:", notas) # Imprimimos la lista de notas ordenadas
print("Hasta luego!") # Mensaje de despedida
