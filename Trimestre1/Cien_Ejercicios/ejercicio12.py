def buscar_palabra(lista, palabra):
    contador = 0
    for p in lista:
        if p == palabra:
            contador += 1
    return contador

palabras = ['hola', 'mundo', 'programación', 'python', 'hola', 'mundo']

palabra = input("Ingrese una palabra para buscar: ")

cantidad_palabra = buscar_palabra(palabras, palabra)
print("Cantidad de veces que aparece la palabra", palabra, "en la lista:", cantidad_palabra)