import math

def mostrar_menu():
    print("\n=== CALCULADORA CIENTÍFICA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Factorial")
    print("8. Seno, Coseno, Tangente")
    print("9. Logaritmo")
    print("0. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                a, b = float(input("a = ")), float(input("b = "))
                print("Resultado:", a + b)
            elif opcion == "2":
                a, b = float(input("a = ")), float(input("b = "))
                print("Resultado:", a - b)
            elif opcion == "3":
                a, b = float(input("a = ")), float(input("b = "))
                print("Resultado:", a * b)
            elif opcion == "4":
                a, b = float(input("a = ")), float(input("b = "))
                if b == 0:
                    print("Error: División entre cero")
                else:
                    print("Resultado:", a / b)
            elif opcion == "5":
                base, exp = float(input("Base = ")), float(input("Exponente = "))
                print("Resultado:", math.pow(base, exp))
            elif opcion == "6":
                num = float(input("Número = "))
                if num < 0:
                    print("Error: No se puede calcular raíz de número negativo")
                else:
                    print("Resultado:", math.sqrt(num))
            elif opcion == "7":
                n = int(input("Número entero = "))
                if n < 0:
                    print("Error: Factorial solo definido para enteros >= 0")
                else:
                    print("Resultado:", math.factorial(n))
            elif opcion == "8":
                ang = math.radians(float(input("Ángulo en grados = ")))
                print("Seno:", math.sin(ang))
                print("Coseno:", math.cos(ang))
                print("Tangente:", math.tan(ang))
            elif opcion == "9":
                num = float(input("Número = "))
                if num <= 0:
                    print("Error: log solo definido para num > 0")
                else:
                    print("Logaritmo natural (ln):", math.log(num))
                    print("Logaritmo base 10:", math.log10(num))
            elif opcion == "0":
                print("Saliendo de la calculadora...")
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Error: entrada inválida, use números válidos.")

if __name__ == "__main__":
    calculadora()