def obtenerPersonajes():
    return [
        {
            "nombre": "Hombre",
            "ascii": "  O  \n /|\ \n / \ ",
        },
        {
            "nombre": "Mujer",
            "ascii": "  O  \n /|\ \n / \ ",
        },
    ]

def obtenerArmaduras():
    return [
        {
            "nombre": "Casco",
            "ascii": "  ^  ",
        },
        {
            "nombre": "Peto",
            "ascii": " /|\ ",
        },
        {
            "nombre": "Pantalón",
            "ascii": "  |  ",
        },
        {
            "nombre": "Botas",
            "ascii": " / \ ",
        },
    ]

def ascii_personaje(personaje, armaduras):
    print(personaje["ascii"])
    for armadura in armaduras:
        print(armadura["ascii"])
