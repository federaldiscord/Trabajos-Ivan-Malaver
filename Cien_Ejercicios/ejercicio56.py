def calcular_costo_pedido_con_envio_gratis_clientes_premium(productos, es_cliente_premium):
    total = 0
    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        descuento = producto["descuento"]
        costo_producto = precio * (1 - descuento)
        total += costo_producto
    if es_cliente_premium:
        valor_envio = 0
    else:
        valor_envio = 10
    costo_total = total + valor_envio
    return costo_total

productos = []
cantidad_productos = int(input("Ingrese la cantidad de productos en el pedido: "))
for i in range(cantidad_productos):
    producto = {}
    producto["nombre"] = input("Ingrese el nombre del producto", i+1, ": ")
    producto["precio"] = float(input("Ingrese el precio del producto", i+1, ": "))
    producto["descuento"] = float(input("Ingrese el porcentaje de descuento del producto", i+1, ": "))
    productos.append(producto)

es_cliente_premium = input("Es cliente premium? (s/n): ")
if es_cliente_premium.lower() == "s":
    es_cliente_premium = True
else:
    es_cliente_premium = False

costo_total = calcular_costo_pedido_con_envio_gratis_clientes_premium(productos, es_cliente_premium)
print("Costo total del pedido:", costo_total)