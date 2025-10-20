# Ordenar y reorganizar una lista de frutas
frutas = ["manzana", "banana", "cereza", "durazno", "pera" , "uva", "kiwi", "mango", "fresa", "naranja"]
print("Lista original de frutas:", frutas) # Imprimimos la lista original
frutas.sort() # Ordenamos la lista de frutas alfabéticamente
print("Lista de frutas ordenada alfabéticamente:", frutas) # Imprimimos la lista ordenada
frutas.reverse() # Invertimos el orden de la lista
print("Lista de frutas en orden inverso:", frutas) # Imprimimos la lista en orden inverso
print("La fruta en la posición 3 es:", frutas[3]) # Imprimimos la fruta en la posición 3
print("La fruta en la posición 7 es:", frutas[7]) # Imprimimos la fruta en la posición 7
print("La fruta en la posición 0 es:", frutas[0]) # Imprimimos la fruta en la posición 0
print("La fruta en la última posición es:", frutas[-1]) # Imprimimos la fruta en la última posición
print("La fruta en la penúltima posición es:", frutas[-2]) # Imprimimos la fruta en la penúltima posición
print("La fruta en la antepenúltima posición es:", frutas[-3]) # Imprimimos la fruta en la antepenúltima posición
print("Cantidad total de frutas en la lista:", len(frutas)) # Imprimimos la cantidad total de frutas en la lista
import random # Importamos la librería random para mezclar la lista
random.shuffle(frutas) # Mezclamos la lista de frutas
print("Lista de frutas mezclada:", frutas) # Imprimimos la lista mezclada