print("¿Quieres saber si eres ganador de un descuento? Dime de cuánto fue el total de la compra.")
compra = float(input("Total de la compra: "))

if compra > 100:
    descuento = compra * 0.10
    total = compra - descuento
    print("Felicidades :D")
else:
    descuento = 0
    total = compra
    print("Lástima, el valor de compra no supera el mínimo para descuento :c")

print(f"Descuento aplicado: ${descuento}")
print(f"Debes pagar: ${total}")