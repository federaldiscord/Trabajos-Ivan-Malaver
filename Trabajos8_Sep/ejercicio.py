with open("ejercicio.txt", "r", encoding="utf-8") as archivo:
    archivo.write("Esta mañana salio el sol por el oriente y es una acción maravillosa")
    contenido = archivo.read()
    print(contenido)