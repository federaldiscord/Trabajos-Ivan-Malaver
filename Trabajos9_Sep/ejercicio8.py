# Clasificador de notas
nota = float(input("Ingrese su nota (0 - 5): ")) # Pedimos al usuario ingresar su nota
if 0 <= nota < 3.5: # Si la nota está entre 0 y menor a 3.5
    print("No aprobado") # Imprimimos que no aprobó
elif 3.5 <= nota < 4.5: # Si la nota está entre 3.5 y menor a 4.5
    print("Aprobado") # Imprimimos que aprobó
elif 4.5 <= nota <= 5: # Si la nota está entre 4.5 y 5
    print("Desempeño excelente") # Imprimimos que es sobresaliente
else: # Si la nota no está en el rango de 0 a 5
    print("Nota inválida, por favor ingrese una nota entre 0 y 5.") # Imprimimos que la nota es inválida