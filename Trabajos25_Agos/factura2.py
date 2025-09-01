productos = ["Manzanas", "Pan", "Leche", "Huevos", "Queso"]
precios = [1.50, 2.00, 1.20, 2.50, 3.80]
iva = 0.19

print("*----------------*")
print("MiniMarket Carry")
print("Carrera 7 # 10-15 Madrid Cund.")
print("NIT: 1230987654567890")
print("*----------------*")
print("Factura:")
print("Producto  | Precio")

num_productos = int(input("¿Cuántos productos va a llevar? (máx. {}): ".format(len(productos))))
while num_productos > len(productos) or num_productos < 1:
	num_productos = int(input("Por favor ingrese un número válido (1-{}): ".format(len(productos))))
for i in range(num_productos):
	print(productos[i], " | ", precios[i])

print("*----------------*")

subtotal = sum(precios[:num_productos])
iva_total = subtotal * iva
total = subtotal + iva_total

print("Subtotal:", subtotal)
print("IVA:", iva_total)
print("Total:", total)
print("*----------------*")

for prod, precio in zip(productos[:num_productos], precios[:num_productos]):
	iva_prod = precio * iva
	print(f"IVA de {prod}: {iva_prod}")
