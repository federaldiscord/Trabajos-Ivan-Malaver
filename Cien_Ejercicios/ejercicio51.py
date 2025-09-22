def calcular_costo_pedido(productos):
    total = 0
    for producto in productos:
        nombre = producto["nombre"]
        precio = producto["precio"]
        descuento = producto["descuento"]
        costo_producto = precio * (1 - descuento)
        total += costo_producto
    return total

def calcular_valor_total_pedido(productos, envio_gratis):
    costo_pedido = calcular_costo_pedido(productos)
    if envio_gratis:
        valor_envio = 0
    else:
        valor_envio = 10
    valor_total = costo_pedido + valor_envio
    return valor_total

productos = []
cantidad_productos = int(input("Ingrese la cantidad de productos en el pedido: "))
for i in range(cantidad_productos):
    producto = {}
    producto["nombre"] = input("Ingrese el nombre del producto", i+1, ": ")
    producto["precio"] = float(input("Ingrese el precio del producto", i+1, ": "))
    producto["descuento"] = float(input("Ingrese el porcentaje de descuento del producto", i+1, ": "))
    productos.append(producto)

envio_gratis = input("Desea el envío gratis? (s/n): ")
if envio_gratis.lower() == "s":
    envio_gratis = True
else:
    envio_gratis = False

valor_total = calcular_valor_total_pedido(productos, envio_gratis)
print("Valor total del pedido:", valor_total)