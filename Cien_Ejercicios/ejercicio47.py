def calcular_salario_final(salario, categoria, horas_trabajadas):
    if categoria == 1:
        tarifa_hora = 10
    elif categoria == 2:
        tarifa_hora = 12
    elif categoria == 3:
        tarifa_hora = 15
    else:
        tarifa_hora = 0

    if horas_trabajadas <= 40:
        salario_final = tarifa_hora * horas_trabajadas
    else:
        horas_extras = horas_trabajadas - 40
        salario_base = tarifa_hora * 40
        salario_extras = tarifa_hora * 1.5 * horas_extras
        salario_final = salario_base + salario_extras

    if salario_final > 1000:
        descuento = 0.1
    else:
        descuento = 0

    salario_final_con_descuento = salario_final * (1 - descuento)
    return salario_final_con_descuento

salario = float(input("Ingrese el salario base del empleado: "))
categoria = int(input("Ingrese la categoría del empleado (1, 2 o 3): "))
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas del empleado: "))

salario_final = calcular_salario_final(salario, categoria, horas_trabajadas)
print("Salario final del empleado con descuento:", salario_final)