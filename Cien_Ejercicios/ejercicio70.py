import random

ciudades = {
    "Bogotá": (4.71, -74.07),
    "Medellín": (6.25, -75.56),
    "Cali": (3.45, -76.53),
}

productos = [
    {"nombre": "Manzanas", "precio": 2.5, "stock": 50},
    {"nombre": "Bananas", "precio": 1.8, "stock": 70},
    {"nombre": "Naranjas", "precio": 3.0, "stock": 40},
    {"nombre": "Peras", "precio": 2.2, "stock": 30},
    {"nombre": "Uvas", "precio": 4.5, "stock": 20},
]

def imprimir_productos(lista):
    """Muestra los productos en formato tabla."""
    print("\nProductos disponibles:")
    print(f"{'Nombre':<10} {'Precio':<8} {'Stock':<6}")
    for p in lista:
        print(f"{p['nombre']:<10} {p['precio']:<8.2f} {p['stock']:<6}")
    print()


def ordenar_productos_por_precio(lista):
    """Ordena los productos usando Inserción (ascendente por precio)."""
    n = len(lista)
    for i in range(1, n):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["precio"] > actual["precio"]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = actual
    return lista


def buscar_producto_binaria(lista, nombre):
    """Búsqueda binaria por nombre en lista de productos (ordenada alfabéticamente)."""
    inicio, final = 0, len(lista) - 1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio]["nombre"].lower() == nombre.lower():
            return medio
        elif lista[medio]["nombre"].lower() < nombre.lower():
            inicio = medio + 1
        else:
            final = medio - 1
    return -1


def calcular_distancia(ciudad1, ciudad2):
    """Distancia ficticia entre dos ciudades (usando coordenadas)."""
    if ciudad1 not in ciudades or ciudad2 not in ciudades:
        return None
    lat1, lon1 = ciudades[ciudad1]
    lat2, lon2 = ciudades[ciudad2]
    return round(((lat1 - lat2)**2 + (lon1 - lon2)**2) ** 0.5 * 111, 2)

imprimir_productos(productos)

productos_ordenados = ordenar_productos_por_precio(productos[:])
print("Productos ordenados por precio:")
imprimir_productos(productos_ordenados)

productos_por_nombre = sorted(productos, key=lambda p: p["nombre"])
nombre_buscar = "Bananas"
indice = buscar_producto_binaria(productos_por_nombre, nombre_buscar)

if indice != -1:
    print(f"✅ El producto '{nombre_buscar}' se encontró en el índice {indice}.")
    print(productos_por_nombre[indice])
else:
    print(f"❌ El producto '{nombre_buscar}' no está disponible.")

c1, c2 = "Bogotá", "Cali"
distancia = calcular_distancia(c1, c2)
print(f"\nLa distancia aproximada entre {c1} y {c2} es {distancia} km.")
