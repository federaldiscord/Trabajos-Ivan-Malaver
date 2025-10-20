primera_lista=["manzana","banana","pera", "naranja", "kiwi", "papaya", "aguacate"]
print(f"{primera_lista} Lista normal")
print(f"{primera_lista[0]} Item en la posicion 0")
print(f"{primera_lista[3:6]} Rango de posiciones 3 a 6")
print(f"{primera_lista[2:4]} Rango de posiciones 2 a 3, porque el 4 no se incluye")
print(f"{primera_lista[-1]} Ultimo item")
print(f"{primera_lista[1:]} Desde la posicion 1 hasta el final")
print(f"{primera_lista[::]} Toda la lista")
print(f"{primera_lista[::-1]} Lista en orden inverso")

primera_lista.append("mango")
print(f"{primera_lista} después de append")

primera_lista.insert(2,"cereza")
print(f"{primera_lista} después de insert en la posicion 2")

primera_lista.extend(["fresa","frambuesa"])
print(f"{primera_lista} agregando dos elementos más al final")

primera_lista.remove("papaya")
print(f"{primera_lista} después de remover `papaya`")

primera_lista.pop()
print(f"{primera_lista} después de hacer pop (remueve el último elemento)")

primera_lista.pop(4)
print(f"{primera_lista} después de hacer pop en la posición 4")

primera_lista.clear()
print(f"{primera_lista} después de clear (limpia la lista)")