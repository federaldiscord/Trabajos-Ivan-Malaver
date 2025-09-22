
libros = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "datos": (1967, 417)},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "datos": (1963, 600)},
    {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "datos": (1985, 348)},
    {"titulo": "Pedro Páramo", "autor": "Juan Rulfo", "datos": (1955, 124)},
    {"titulo": "Ficciones", "autor": "Jorge Luis Borges", "datos": (1944, 174)},
]



def imprimir_libros(lista):
    """Muestra los libros en formato tabla."""
    print(f"\n{'Título':<35} {'Autor':<25} {'Año':<6} {'Páginas':<8}")
    print("-"*80)
    for libro in lista:
        anio, paginas = libro["datos"]
        print(f"{libro['titulo']:<35} {libro['autor']:<25} {anio:<6} {paginas:<8}")
    print()


def ordenar_por_anio(lista):
    """Ordena libros usando inserción por año (ascendente)."""
    n = len(lista)
    for i in range(1, n):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["datos"][0] > actual["datos"][0]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = actual
    return lista


def buscar_binaria_titulo(lista, titulo):
    """Búsqueda binaria por título (lista ordenada alfabéticamente)."""
    inicio, final = 0, len(lista) - 1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio]["titulo"].lower() == titulo.lower():
            return medio
        elif lista[medio]["titulo"].lower() < titulo.lower():
            inicio = medio + 1
        else:
            final = medio - 1
    return -1



print("📚 Lista de libros en la biblioteca:")
imprimir_libros(libros)

libros_ordenados_anio = ordenar_por_anio(libros[:])
print("📖 Libros ordenados por año de publicación:")
imprimir_libros(libros_ordenados_anio)

libros_ordenados_titulo = sorted(libros, key=lambda l: l["titulo"])
titulo_buscar = "Rayuela"
indice = buscar_binaria_titulo(libros_ordenados_titulo, titulo_buscar)

if indice != -1:
    print(f"✅ El libro '{titulo_buscar}' se encontró en el índice {indice}:")
    print(libros_ordenados_titulo[indice])
else:
    print(f"❌ El libro '{titulo_buscar}' no está en la biblioteca.")
