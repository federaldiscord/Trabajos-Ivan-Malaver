# Descuento por compra
precio = float(input("Ingrese el precio del producto: ")) # Solicitamos el precio del producto

if precio > 100: # Verificamos si el precio es mayor a 100
    descuento = precio * 0.15 # Calculamos el descuento del 15%
    precio_final = precio - descuento # Calculamos el precio final con descuento
    print(f"El precio final con descuento es: {precio_final}") # Imprimimos
    print(f"El precio original era: {precio}") # Imprimimos el precio original
    print(f"Has ahorrado: {descuento}") # Imprimimos el ahorro
else: # Si el precio no es mayor a 100
    print(f"El precio final es: {precio}") # Imprimimos el precio sin descuento