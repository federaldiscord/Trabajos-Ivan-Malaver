vacaciones = input("¿Qué tipo de vacaciones prefieres? (playa, montaña, ciudad): ").lower()

if vacaciones == "playa":
    print("Te recomiendo visitar Cancún para disfrutar del mar y la arena.")
elif vacaciones == "montaña":
    print("Escoge los Andes para hacer senderismo y ver paisajes impresionantes.")
elif vacaciones == "ciudad":
    print("Visita Barcelona por su arquitectura y vida cultural.")
else:
    print("Prueba algo nuevo: explora destinos rurales o viajes de aventura.")