import random

libros = [
    {"titulo": "Cien Años de Soledad", "paginas": 417},
    {"titulo": "Don Quijote de la Mancha", "paginas": 863},
    {"titulo": "1984", "paginas": 328},
    {"titulo": "El Señor de los Anillos", "paginas": 1216},
    {"titulo": "La Odisea", "paginas": 541}
]

def ordenar_por_paginas(lista):
    return sorted(lista, key=lambda x: x["paginas"])

def buscar_libro(lista, titulo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio]["titulo"].lower() == titulo.lower():
            return medio
        elif lista[medio]["titulo"].lower() < titulo.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

print("Lista de libros:")
for l in libros:
    print(l["titulo"], "-", l["paginas"], "páginas")

print("\nLibros ordenados por páginas:")
ordenados = ordenar_por_paginas(libros)
for l in ordenados:
    print(l["titulo"], "-", l["paginas"], "páginas")

print("\nBúsqueda de libro:")
libros_ordenados_titulo = sorted(libros, key=lambda x: x["titulo"])
indice = buscar_libro(libros_ordenados_titulo, "1984")
if indice != -1:
    print("Encontrado:", libros_ordenados_titulo[indice])
else:
    print("No encontrado")
