archivo = open("factura.txt", "w")
archivo.write("Factura de Compra\n")
archivo.write("=================\n")
archivo.write(input("Ingrese su nombre: ") + "\n")
archivo.write("Productos:\n")

while True:
    archivo.write(input("Producto: ") + "\n")
    archivo.write(input("Precio: ") + "\n")
    respuesta = input("¿Desea añadir más productos? (s/n): ")
    if respuesta.lower() != 's':
        break
archivo.write("=================\n")
archivo.write("Subtotal: " + input("Subtotal: ") + "\n")
archivo.write("IVA: " + input("IVA: ") + "\n")
archivo.write("Total: " + input("Total: ") + "\n")
archivo.close()

archivo = open("factura.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
