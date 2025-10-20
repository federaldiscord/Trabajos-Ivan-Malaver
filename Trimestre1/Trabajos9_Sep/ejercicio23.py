# Analizador de texto
def contadorPalabras(texto):
    # Cuenta la cantidad de palabras en el texto
    palabras = texto.split() # Dividimos el texto en palabras usando espacios como separadores
    return len(palabras) # Retornamos la cantidad de palabras
def contadorCaracteres(texto):
    # Cuenta la cantidad de caracteres en el texto (incluyendo espacios)
    return len(texto) # Retornamos la cantidad de caracteres
def contadorVocales(texto):
    # Cuenta la cantidad de vocales en el texto
    vocales = "aeiouAEIOU" # Definimos las vocales (mayúsculas y minúsculas)
    return sum(1 for char in texto if char in vocales) # Contamos y retornamos la cantidad de vocales
def contarPalabraLarga(texto):
    # Encuentra la palabra más larga en el texto
    palabras = texto.split() # Dividimos el texto en palabras usando espacios como separadores
    if not palabras: # Si la lista de palabras está vacía
        return 0 # Retornamos 0
    palabra_mas_larga = max(palabras, key=len) # Encontramos la palabra más larga usando la función max con la longitud como clave
    return len(palabra_mas_larga) # Retornamos la longitud de la palabra más larga 

palabra = str(input("Por favor ingrese un texto: ")) # Pedimos al usuario ingresar un texto
print(f"El texto ingresado tiene {contadorPalabras(palabra)} palabras.") # Imprimimos la cantidad de palabras
print(f"El texto ingresado tiene {contadorCaracteres(palabra)} caracteres.") # Imprimimos la cantidad de caracteres
print(f"El texto ingresado tiene {contadorVocales(palabra)} vocales.") # Imprimimos la cantidad de vocales
print(f"La palabra más larga tiene {contarPalabraLarga(palabra)} caracteres.") # Imprimimos la longitud de la palabra más larga