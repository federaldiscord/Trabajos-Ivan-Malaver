def calcular_media_notas(notas):
    suma_notas = sum(notas)
    cantidad_notas = len(notas)
    media = suma_notas / cantidad_notas
    return media

def verificar_aprobo_reprobo(media):
    if media >= 4:
        return "Aprobado"
    else:
        return "Reprobado"

notas = []
cantidad_notas = int(input("Ingrese la cantidad de notas: "))
for i in range(cantidad_notas):
    nota = float(input("Ingrese la nota", i+1, ": "))
    notas.append(nota)

media = calcular_media_notas(notas)
resultado = verificar_aprobo_reprobo(media)
print("Media de las notas:", media)
print("Resultado:", resultado)