primera_lista=["manzana","banana","pera", "naranja", "kiwi", "papaya", "aguacate"]
for i in primera_lista:
     print(i)
print("-----")

for pos, lista in enumerate(primera_lista):
     print(f"La fruta {lista} está en la posición {pos}")

print("-----")

for i in range(2, 6):
    print(primera_lista[i])

print("-----")

var = "papaya" in primera_lista
print(var)

vr4 = primera_lista.index("kiwi")
print(vr4)