def calcular_similitud(usuario1, usuario2):
    gustos_comunes = 0
    total_comparaciones = 0

    for categoria in usuario1:
        if categoria in usuario2:
            total_comparaciones += 1
            if usuario1[categoria] == usuario2[categoria]:
                gustos_comunes += 1

    if total_comparaciones == 0:
        return 0

    similitud = gustos_comunes / total_comparaciones
    return round(similitud, 2)


def encontrar_usuarios_similares(usuario_objetivo, base_usuarios, umbral=0.6):
    similares = []
    print(f"Buscando usuarios similares a '{usuario_objetivo}'")
    print(f"Umbral de similitud: {umbral}")
    print("-" * 40)

    gustos_objetivo = base_usuarios[usuario_objetivo]
    for nombre_usuario, gustos_usuario in base_usuarios.items():
        if nombre_usuario != usuario_objetivo:
            similitud = calcular_similitud(gustos_objetivo, gustos_usuario)
            print(f"{nombre_usuario}: similitud = {similitud}")
            if similitud >= umbral:
                similares.append((nombre_usuario, similitud))

    similares.sort(key=lambda x: x[1], reverse=True)
    return similares


def recomendar_contenido(usuario_objetivo, usuarios_similares, base_usuarios):
    """
    Recomienda contenido basado en usuarios similares
    """
    gustos_objetivo = base_usuarios[usuario_objetivo]
    recomendaciones = {}

    print(f"\nGenerando recomendaciones para '{usuario_objetivo}':")
    for nombre_similar, similitud in usuarios_similares:
        gustos_similar = base_usuarios[nombre_similar]
        print(f"\nAnalizando gustos de {nombre_similar} (similitud: {similitud}):")
        for categoria, le_gusta in gustos_similar.items():
            if categoria not in gustos_objetivo and le_gusta:
                if categoria not in recomendaciones:
                    recomendaciones[categoria] = []
                recomendaciones[categoria].append((nombre_similar, similitud))
                print(f"  → Recomendar '{categoria}' (le gusta a {nombre_similar})")
    return recomendaciones


usuarios = {
    "Ana": {
        "acción": True, "comedia": True, "drama": False,
        "terror": False, "ciencia_ficción": True
    },
    "Carlos": {
        "acción": True, "comedia": False, "drama": True,
        "terror": False, "ciencia_ficción": True
    },
    "María": {
        "acción": False, "comedia": True, "drama": True,
        "terror": True, "ciencia_ficción": False
    },
    "Pedro": {
        "acción": True, "comedia": True, "drama": False,
        "terror": False, "ciencia_ficción": False
    },
    "Laura": {
        "acción": False, "comedia": True, "drama": True,
        "terror": False, "ciencia_ficción": True
    }
}

print("SISTEMA DE RECOMENDACIONES")
print("=" * 35)

print("Base de usuarios:")
for usuario, gustos in usuarios.items():
    print(f"{usuario}: {gustos}")

print("\n" + "=" * 50)

usuario_objetivo = "Ana"
similares = encontrar_usuarios_similares(usuario_objetivo, usuarios, 0.4)
print(f"\nUsuarios similares a {usuario_objetivo}:")
for similar, similitud in similares:
    print(f"  {similar}: {similitud * 100:.0f}% similar")

recomendaciones = recomendar_contenido(usuario_objetivo, similares, usuarios)
print("\n" + "=" * 30)
print("RECOMENDACIONES FINALES")
print("=" * 30)
if recomendaciones:
    for categoria, recomendadores in recomendaciones.items():
        print(f"{categoria}: recomendado por {[u for u, _ in recomendadores]}")
else:
    print("No hay recomendaciones disponibles.")