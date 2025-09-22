def calcular_valor_articulo(precio, descuento):
    valor = precio * (1 - descuento)
    return valor

def calcular_valor_total_carrito(carrito):
    total = 0
    for articulo in carrito:
        total += calcular_valor_articulo(articulo['precio'], articulo['descuento'])
    return total

carrito = []
cantidad_articulos = int(input("Ingrese la cantidad de artículos en el carrito: "))
for i in range(cantidad_articulos):
    articulo = {}
    articulo['nombre'] = input("Ingrese el nombre del artículo: ")
    articulo['precio'] = float(input("Ingrese el precio del artículo: "))
    articulo['descuento'] = float(input("Ingrese el porcentaje de descuento del artículo: "))
    carrito.append(articulo)

valor_total = calcular_valor_total_carrito(carrito)
print("Valor total del carrito con descuento:", valor_total)