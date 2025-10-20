import random

productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 10},
    {"nombre": "Teléfono", "precio": 800, "stock": 25},
    {"nombre": "Auriculares", "precio": 150, "stock": 40},
    {"nombre": "Monitor", "precio": 300, "stock": 15},
    {"nombre": "Teclado", "precio": 100, "stock": 50}
]

def calcular_valor_inventario(producto):
    return producto["precio"] * producto["stock"]

def ordenar_por_precio(lista):
    return sorted(lista, key=lambda p: p["precio"])

def buscar_binaria(lista, nombre):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio]["nombre"].lower() == nombre.lower():
            return medio
        elif lista[medio]["nombre"].lower() < nombre.lower():
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def imprimir_productos(lista):
    for p in lista:
        print(f"{p['nombre']} - Precio: {p['precio']} - Stock: {p['stock']} - Valor total: {calcular_valor_inventario(p)}")

print("Inventario inicial:")
imprimir_productos(productos)

print("\nInventario ordenado por precio:")
productos_ordenados = ordenar_por_precio(productos)
imprimir_productos(productos_ordenados)

print("\nBúsqueda de producto:")
productos_ordenados_nombre = sorted(productos, key=lambda p: p["nombre"])
indice = buscar_binaria(productos_ordenados_nombre, "Monitor")
if indice != -1:
    print("Producto encontrado:", productos_ordenados_nombre[indice])
else:
    print("Producto no encontrado")
