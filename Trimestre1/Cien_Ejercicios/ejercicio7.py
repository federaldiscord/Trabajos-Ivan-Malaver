def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto = input("Ingrese un texto: ")

cantidad_palabras = contar_palabras(texto)
print("Cantidad de palabras en el texto:", cantidad_palabras)