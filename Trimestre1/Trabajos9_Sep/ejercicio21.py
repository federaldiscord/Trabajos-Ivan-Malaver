def saludar():
 # Saluda a una persona por su nombre y apellido
    nombre = input("Por favor ingrese su nombre: ") # Pedimos al usuario ingresar su nombre
    apellido = input("Por favor ingrese su apellido: ") # Pedimos al usuario ingresar su apellido
    print(f"Hola, {nombre} {apellido}. ¿Cómo estás?") # Imprimimos el saludo con el nombre y apellido
saludar() # Llamamos a la función para ejecutar el saludo
