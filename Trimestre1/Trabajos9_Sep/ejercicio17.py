# Lista de compras inteligente con menú
lista_compras = []

def mostrar_lista():
    print("\nTu lista de compras es:")
    if not lista_compras:
        print("  (Vacía :c)")
    else:
        for i, item in enumerate(lista_compras, 1):
            print(f"{i}. {item}")

while True:
    print("\nMenú:")
    print("1. Añadir artículo")
    print("2. Eliminar artículo")
    print("3. Modificar artículo")
    print("4. Mostrar lista")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        articulo = input("Ingrese el artículo a añadir: ")
        lista_compras.append(articulo)
        print(f"'{articulo}' añadido a la lista.")
    elif opcion == '2':
        mostrar_lista()
        idx = input("Ingrese el número del artículo a eliminar: ")
        if idx.isdigit() and 1 <= int(idx) <= len(lista_compras):
            eliminado = lista_compras.pop(int(idx)-1)
            print(f"'{eliminado}' eliminado de la lista.")
        else:
            print("Número inválido.")
    elif opcion == '3':
        mostrar_lista()
        idx = input("Ingrese el número del artículo a modificar: ")
        if idx.isdigit() and 1 <= int(idx) <= len(lista_compras):
            nuevo = input("Ingrese el nuevo nombre del artículo: ")
            lista_compras[int(idx)-1] = nuevo
            print("Artículo modificado.")
        else:
            print("Número inválido.")
    elif opcion == '4':
        mostrar_lista()
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")