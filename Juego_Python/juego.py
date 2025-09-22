from diccionarios import personajes, armaduras
from listas import opci_personaje, opci_armadura
from funciones import ascii_personaje

print("Bienvenido al combate por rondas orientado en RPG! \n Recuerda que cada ronda puedes cambiar de personaje y armadura.")
print("Elige tu personaje según quieras luchar esta ronda:")
for i, opcion in enumerate(opci_personaje):
    print(f"{i+1}. {personajes[opcion]['nombre']}")

personaje_idx = int(input("Selecciona (1 o 2): ")) - 1
personaje_elegido = personajes[opci_personaje[personaje_idx]]

print("\nElige tu armadura:")
for i, opcion in enumerate(opci_armadura):
    print(f"{i+1}. {armaduras[opcion]['nombre']}")

armaduras_elegidas = []
for i in range(len(opci_armadura)):
    respuesta = input(f"¿Quieres equipar {armaduras[opci_armadura[i]]['nombre']}? (s/n): ")
    if respuesta.lower() == 's':
        armaduras_elegidas.append(armaduras[opci_armadura[i]])

print("\nTu personaje equipado:")
ascii_personaje(personaje_elegido, armaduras_elegidas)

print("¡Que comience la batalla!")
