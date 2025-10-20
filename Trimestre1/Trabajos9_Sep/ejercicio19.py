# Buscador en la lista
lista = ["manzana", "banana", "cereza", "durazno", "pera" , "uva", "kiwi", "mango", "fresa", "naranja"]
fruta_buscada = input("Ingrese el nombre de la fruta que desea buscar: ").lower() # Pedimos al usuario ingresar el nombre de la fruta y lo convertimos a minúsculas
if fruta_buscada in [fruta.lower() for fruta in lista]: # Verificamos si la fruta está en la lista (ignorando mayúsculas/minúsculas)
    print(f"La fruta '{fruta_buscada}' está en la lista.") # Imprimimos que la fruta está en la lista
else: # Si la fruta no está en la lista 
    print(f"La fruta '{fruta_buscada}' no está en la lista.") # Imprimimos que la fruta no está en la lista
# Buscar multiples frutas
frutas_buscadas = input("Ingrese los nombres de las frutas que desea buscar, separadas por comas: ").split(",") # Pedimos al usuario ingresar los nombres de las frutas separados por comas
frutas_buscadas = [fruta.strip().lower() for fruta in frutas_buscadas] # Limpiamos espacios y convertimos a minúsculas
frutas_encontradas = [fruta for fruta in frutas_buscadas if fruta in [f.lower() for f in lista]] # Buscamos las frutas que están en la lista
frutas_no_encontradas = [fruta for fruta in frutas_buscadas if fruta not in [f.lower() for f in lista]] # Buscamos las frutas que no están en la lista
if frutas_encontradas: # Si encontramos frutas en la lista
    print("Las siguientes frutas están en la lista:", ", ".join(frutas_encontradas)) # Imprimimos las frutas encontradas
if frutas_no_encontradas: # Si no encontramos algunas frutas en la lista
    print("Las siguientes frutas no están en la lista:", ", ".join(frutas_no_encontradas)) # Imprimimos las frutas no encontradas