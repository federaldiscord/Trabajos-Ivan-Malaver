def calcular_valor_pedido(productos):
    total = 0
    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        descuento = producto["descuento"]
        valor_producto = precio * (1 - descuento)
        total += valor_producto
    return total

productos = []
cantidad_productos = int(input("Ingrese la cantidad de productos en el pedido: "))
for i in range(cantidad_productos):
    producto = {}
    producto["nombre"] = input("Ingrese el nombre del producto", i+1, ": ")
    producto["precio"] = float(input("Ingrese el precio del producto", i+1, ": "))
    producto["descuento"] = float(input("Ingrese el porcentaje de descuento del producto", i+1, ": "))
    productos.append(producto)

valor_pedido = calcular_valor_pedido(productos)
print("Valor total del pedido:", valor_pedido)