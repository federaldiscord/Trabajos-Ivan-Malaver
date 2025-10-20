import random

def calcular_distancia(ciudad_origen, ciudad_destino):
    """
    Simula la distancia entre dos ciudades.
    En un caso real se podría integrar con un API de mapas.
    """
    return random.randint(50, 2000)

def calcular_tiempo_entrega(ciudad_origen, ciudad_destino, distancia, tipo_envio):
    if tipo_envio == "express":
        tiempo_entrega = distancia / 100 + random.uniform(0, 2)
    elif tipo_envio == "estandar":
        tiempo_entrega = distancia / 80 + random.uniform(0, 3)
    elif tipo_envio == "económico":
        tiempo_entrega = distancia / 120 + random.uniform(0, 4)
    else:
        print("Tipo de envío inválido")
        return None
    return round(tiempo_entrega, 2)

def calcular_costo_pedido(productos, tipo_envio):
    total = 0
    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        descuento = producto["descuento"] / 100
        costo_producto = precio * (1 - descuento)
        total += costo_producto
    
    if tipo_envio == "express":
        costo_envio = 20
    elif tipo_envio == "estandar":
        costo_envio = 10
    elif tipo_envio == "económico":
        costo_envio = 5
    else:
        print("Tipo de envío inválido")
        return None
    
    costo_total = total + costo_envio
    return round(costo_total, 2)

def ordenar_productos_por_precio(productos):
    return sorted(productos, key=lambda x: x["precio"], reverse=True)

def buscar_producto_por_nombre(nombre, productos):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

productos = []
cantidad_productos = int(input("Ingrese la cantidad de productos en el pedido: "))

for i in range(cantidad_productos):
    print(f"\nProducto {i+1}:")
    producto = {}
    producto["nombre"] = input("Ingrese el nombre del producto: ")
    producto["precio"] = float(input("Ingrese el precio del producto: "))
    producto["descuento"] = float(input("Ingrese el porcentaje de descuento del producto (%): "))
    productos.append(producto)

ciudad_origen = input("\nIngrese la ciudad de origen del pedido: ")
ciudad_destino = input("Ingrese la ciudad de destino del pedido: ")

tipo_envio = input("Ingrese el tipo de envío (express, estandar, económico): ").lower()

distancia = calcular_distancia(ciudad_origen, ciudad_destino)

tiempo_entrega = calcular_tiempo_entrega(ciudad_origen, ciudad_destino, distancia, tipo_envio)
costo_total = calcular_costo_pedido(productos, tipo_envio)

if tiempo_entrega is not None and costo_total is not None:
    print("\n============================")
    print(f"Pedido desde {ciudad_origen} hasta {ciudad_destino}")
    print(f"Distancia estimada: {distancia} km")
    print(f"Tiempo de entrega: {tiempo_entrega} días")
    print(f"Costo total del pedido: ${costo_total}")
    print("============================")

ordenar_productos_por_precio(productos)

producto_encontrado = buscar_producto_por_nombre("Producto a buscar", productos)
if producto_encontrado:
    print(f"Producto encontrado: {producto_encontrado}")
else:
    print("Producto no encontrado")