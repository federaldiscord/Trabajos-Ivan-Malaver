from funcionesFactura import (
    calcular_subtotal,
    calcular_cantidad,
    calcular_iva,
    calcular_total,
    iva_por_producto
)
from diccionarioArticulos import articulos
from tuplaArticulos import obtener_tupla_articulos

iva = 0.19

nombre = input("Ingrese su nombre: ")

tupla_articulos = obtener_tupla_articulos(articulos)

print("Productos disponibles:")
for i, (prod, precio) in enumerate(tupla_articulos, 1):
    print(f"{i}. {prod} - ${precio}")

seleccion = input("Ingrese los números de los productos que desea (separados por coma): ")
indices = [int(x.strip()) for x in seleccion.split(",")]

productos = []
precios = []
for idx in indices:
    prod, precio = tupla_articulos[idx - 1]
    productos.append(prod)
    precios.append(precio)

print("*----------------*")
print("Supermercado La Tarea")
print("Calle 8 # 20-30 Bogotá")
print("NIT: 9876543210123456")
print("*----------------*")
print(f"Factura para: {nombre}")
print("Producto  | Precio")
for prod, precio in zip(productos, precios):
    print(f"{prod}  |  {precio}")

print("*----------------*")

subtotal = calcular_subtotal(precios)
iva_total = calcular_iva(subtotal, iva)
total = calcular_total(subtotal, iva_total)

print("Subtotal:", subtotal)
print("IVA:", iva_total)
print("Total:", total)
print("*----------------*")

ivas_prod = iva_por_producto(precios, iva)
for prod, iva_p in zip(productos, ivas_prod):
    print(f"IVA de {prod}: {iva_p}")
