print("Ingresa un año que sea un entero positivo:")
ano = int(input())

if ano <= 0:
    print("Año no válido. Debe ser mayor que 0.")
else:
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print(f"{ano} es bisiesto.")
            else:
                print(f"{ano} no es bisiesto.")
        else:
            print(f"{ano} es bisiesto.")
    else:
        print(f"{ano} no es bisiesto.")