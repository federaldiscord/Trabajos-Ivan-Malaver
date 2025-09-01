nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

archivo = open("dic.txt", "w")
archivo.write(f"Nombre: {nombre}, Edad: {edad}\n")
archivo.close()