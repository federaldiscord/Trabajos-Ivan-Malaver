def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

op = input("¿Convertir a Fahrenheit(F) o a Celsius(C)?: ").lower()
temp = float(input("Ingrese la temperatura: "))

if op == 'f':
    print(f"{temp}°C = {celsius_a_fahrenheit(temp):.2f}°F")
elif op == 'c':
    print(f"{temp}°F = {fahrenheit_a_celsius(temp):.2f}°C")
else:
    print("Opción inválida")