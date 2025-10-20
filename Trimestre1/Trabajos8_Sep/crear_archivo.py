'''
archivo = open("archivo.txt", "w")
archivo.write("Este es un archivo de ejemplo.")
archivo.close
'''

archivo = open("archivo.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

archivo = open("archivo.txt", "a")
archivo.write("\nAñadiendo una nueva línea al archivo.")
archivo.close()

archivo = open("archivo.txt", "r")
contenido = archivo.read()
for line in contenido.splitlines():
    print(line)
archivo.close()