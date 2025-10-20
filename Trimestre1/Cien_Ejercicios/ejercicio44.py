def calcular_costo_pedido(cantidad, precio_unitario, descuento):
    costo_total = cantidad * precio_unitario * (1 - descuento)
    return costo_total

cantidad = int(input("Ingrese la cantidad de productos: "))
precio_unitario = float(input("Ingrese el precio unitario de los productos: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

costo_total = calcular_costo_pedido(cantidad, precio_unitario, descuento)
print("Costo total del pedido:", costo_total)