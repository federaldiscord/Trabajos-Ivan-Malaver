# Primera lista
lista = ["manzana", "banana", "cereza", "durazno", "pera" , "uva", "kiwi", "mango", "fresa", "naranja"]
print("Mi lista de frutas es:", lista) # Imprimimos la lista original

print("Mis frutas favoritas son:") # Indicamos que vamos a listar las frutas favoritas
for fruta in range(0, len(lista), 2): # Bucle que recorre la lista con un paso de 2
    print(lista[fruta]) # Imprimimos las frutas en las posiciones pares

print("La fruta que está en posición 8 es:", lista[8]) # Imprimimos la fruta en la posición 8
