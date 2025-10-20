import random

libros = [
    {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "paginas": 471},
    {"titulo": "1984", "autor": "George Orwell", "paginas": 328},
    {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "paginas": 863},
    {"titulo": "La Odisea", "autor": "Homero", "paginas": 541},
    {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "paginas": 194}
]

def ordenar_por_paginas(lista):
    return sorted(lista, key=lambda l: l["paginas"])

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

print("Catálogo de libros:")
for l in libros:
    print(l["titulo"], "-", l["autor"], "-", l["paginas"], "páginas")

print("\nLibros ordenados por páginas:")
ordenados = ordenar_por_paginas(libros)
for l in ordenados:
    print(l["titulo"], l["paginas"])

print("\nBúsqueda de libro:")
libros_ordenados_titulo = sorted(libros, key=lambda l: l["titulo"])
indice = buscar_libro(libros_ordenados_titulo, "1984")
if indice != -1:
    print("Encontrado:", libros_ordenados_titulo[indice])
else:
    print("No encontrado")
