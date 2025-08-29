import time

print("Vamos a saber si un número es positivo o negativo.")
valor = float(input("Digita el valor: "))
print("Pensando...")
time.sleep(3)

if valor >= 1:
    print("El número es positivo")
elif valor == 0:
    print("El número es cero")
else:
    print("El número es negativo")