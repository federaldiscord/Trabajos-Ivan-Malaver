def calcular_nota_final(examenes, trabajos):
    nota_examenes = sum(examenes) / len(examenes)
    nota_trabajos = sum(trabajos) / len(trabajos)
    nota_final = (0.6 * nota_examenes) + (0.4 * nota_trabajos)
    return nota_final

examenes = []
cantidad_examenes = int(input("Ingrese la cantidad de exámenes: "))
for i in range(cantidad_examenes):
    examen = float(input("Ingrese la nota del examen", i+1, ": "))
    examenes.append(examen)

trabajos = []
cantidad_trabajos = int(input("Ingrese la cantidad de trabajos: "))
for i in range(cantidad_trabajos):
    trabajo = float(input("Ingrese la nota del trabajo", i+1, ": "))
    trabajos.append(trabajo)

nota_final = calcular_nota_final(examenes, trabajos)
print("Nota final del estudiante:", nota_final)

if nota_final >= 4:
    print("El estudiante aprueba")
else:
    print("El estudiante reprueba")