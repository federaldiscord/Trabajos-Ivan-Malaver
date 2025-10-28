hectareas = int(0)
hectareas = int(input("Ingrese la cantidad de hectáreas: "))
if hectareas <= 0:
        print(f"Las hectáreas deben estar dentro del límite (1 - 100), estás ingresando un total de: {hectareas}")
elif hectareas > 100:
        print(f"Parece que las hectáreas superan el valor límite (100), teniendo un total de: {hectareas}")
elif hectareas == 100: 
        print(f"Las hectáreas están al límite, hay un total de: {hectareas}")
else:
        print(f"Las hectáreas están dentro del límite permitido, teniendo un total de: {hectareas}")