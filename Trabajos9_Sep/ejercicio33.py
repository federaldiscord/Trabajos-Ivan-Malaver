import random
import time

def crear_tablero(filas, columnas, densidad=0.3):
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            esta_viva = 1 if random.random() < densidad else 0
            fila.append(esta_viva)
        tablero.append(fila)
    return tablero

def contar_vecinos_vivos(tablero, fila, columna):
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for df, dc in direcciones:
        nueva_fila = fila + df
        nueva_columna = columna + dc
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            vecinos_vivos += tablero[nueva_fila][nueva_columna]
    return vecinos_vivos

def aplicar_reglas(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    cambios = []
    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos_vivos(tablero, i, j)
            celula_actual = tablero[i][j]
            nueva_celula = celula_actual
            if celula_actual == 1:
                if vecinos < 2:
                    nueva_celula = 0
                    cambios.append((i, j, "murió por soledad"))
                elif vecinos > 3:
                    nueva_celula = 0
                    cambios.append((i, j, "murió por sobrepoblación"))
            else:
                if vecinos == 3:
                    nueva_celula = 1
                    cambios.append((i, j, "nació"))
            nuevo_tablero[i][j] = nueva_celula
    return nuevo_tablero, cambios

def mostrar_tablero(tablero, generacion, mostrar_coordenadas=False):
    print(f"\nGeneración {generacion}")
    print("=" * (len(tablero[0]) * 2))
    for i, fila in enumerate(tablero):
        linea = ""
        for j, celula in enumerate(fila):
            simbolo = "⬛" if celula == 1 else "⬜"
            if mostrar_coordenadas:
                linea += f"{i},{j}:{simbolo} "
            else:
                linea += simbolo + " "
        print(linea)

def simular_juego(filas=10, columnas=10, generaciones=5, pausa=1):
    tablero = crear_tablero(filas, columnas)
    for gen in range(1, generaciones + 1):
        mostrar_tablero(tablero, gen)
        tablero, cambios = aplicar_reglas(tablero)
        if cambios:
            print("Cambios en esta generación:")
            for c in cambios:
                print(f" - Celda {c[0]},{c[1]} {c[2]}")
        else:
            print("Sin cambios: estado estable alcanzado")
            break
        time.sleep(pausa)

if __name__ == "__main__":
    simular_juego(filas=8, columnas=8, generaciones=10, pausa=0.5)
