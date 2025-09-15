# Ordenamiento de burbuja
def orde_burbu(Lista):
    x = len(Lista)
    for i in range(x):
        for j in range(0, x-i-1):
            if Lista[j] > Lista[j+1]:
                Lista[j], Lista[j+1] = Lista[j+1], Lista[j]
    return Lista
Lista = [22 , 1, 80, 5, 3, 10, 7, 4, 9, 6, 8, 19, 11, 15, 14, 13, 12, 18, 17, 16]
copia = Lista.copy()
comparaciones = 0
intercambios = 0

print ("Lista original:", copia)
ordenada = orde_burbu(copia)
print ("Lista ordenada:", ordenada)
