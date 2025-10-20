import random

productos = [
    {"nombre": "Manzana", "categoria": "Fruta", "precio": round(random.uniform(0.5, 3), 2)},
    {"nombre": "Leche", "categoria": "Lácteo", "precio": round(random.uniform(0.8, 2.5), 2)},
    {"nombre": "Pan", "categoria": "Panadería", "precio": round(random.uniform(1, 4), 2)},
    {"nombre": "Arroz", "categoria": "Grano", "precio": round(random.uniform(2, 6), 2)},
    {"nombre": "Huevos", "categoria": "Proteína", "precio": round(random.uniform(1.5, 5), 2)}
]

def ordenar_por_precio(lista):
    return sorted(lista, key=lambda p: p["precio"])

def buscar_producto(lista, nombre):
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

print("Lista de productos:")
for p in productos:
    print(p["nombre"], "-", p["categoria"], "-", p["precio"], "USD")

print("\nProductos ordenados por precio:")
ordenados = ordenar_por_precio(productos)
for p in ordenados:
    print(p["nombre"], p["precio"])

print("\nBúsqueda de producto:")
productos_ordenados_nombre = sorted(productos, key=lambda p: p["nombre"])
indice = buscar_producto(productos_ordenados_nombre, "Arroz")
if indice != -1:
    print("Encontrado:", productos_ordenados_nombre[indice])
else:
    print("No encontrado")
