import re 

def analizar_estructura(texto):
    estadisticas = {
        'caracteres_total': len(texto),
        'caracteres_sin_espacios': len(texto.replace(' ', '')),
        'palabras': len(texto.split()),
        'oraciones': len([s for s in texto.split('.') if s.strip()]),
        'párrafos': len([p for p in texto.split('\n\n') if p.strip()])
    }
    return estadisticas


def encontrar_patrones_email(texto):
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(patron_email, texto)


def encontrar_patrones_telefono(texto):
    patrones = [
        r'\b\d{3}-\d{3}-\d{4}\b',
        r'\b\(\d{3}\)\s?\d{3}-\d{4}\b',
        r'\b\d{10}\b'
    ]
    telefonos = []
    for patron in patrones:
        telefonos.extend(re.findall(patron, texto))
    return telefonos


def analizar_sentimiento_basico(texto):
    palabras_positivas = [
        'excelente', 'genial', 'fantástico', 'increíble', 'perfecto',
        'bueno', 'feliz', 'contento', 'alegre', 'maravilloso'
    ]
    palabras_negativas = [
        'terrible', 'malo', 'horrible', 'triste', 'enojado',
        'molesto', 'frustrado', 'decepcionado', 'pesimo'
    ]
    texto_lower = texto.lower()
    puntuacion_positiva = sum(1 for palabra in palabras_positivas if palabra in texto_lower)
    puntuacion_negativa = sum(1 for palabra in palabras_negativas if palabra in texto_lower)

    if puntuacion_positiva > puntuacion_negativa:
        sentimiento = "Positivo"
    elif puntuacion_negativa > puntuacion_positiva:
        sentimiento = "Negativo"
    else:
        sentimiento = "Neutral"

    return {
        'sentimiento': sentimiento,
        'palabras_positivas_encontradas': puntuacion_positiva,
        'palabras_negativas_encontradas': puntuacion_negativa
    }


def encontrar_palabras_repetidas(texto, min_longitud=4):
    palabras = re.findall(r'\b\w+\b', texto.lower())
    palabras_largas = [p for p in palabras if len(p) >= min_longitud]
    frecuencias = {}
    for palabra in palabras_largas:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return {palabra: freq for palabra, freq in frecuencias.items() if freq > 1}


def generar_resumen_legible(estadisticas):
    est = estadisticas
    promedio_palabras_oracion = est['palabras'] / max(est['oraciones'], 1)
    resumen = []
    resumen.append(f"Este texto tiene {est['caracteres_total']} caracteres en total")
    resumen.append(f"Contiene {est['palabras']} palabras distribuidas en {est['oraciones']} oraciones")
    resumen.append(f"El promedio es de {promedio_palabras_oracion:.1f} palabras por oración")
    if est['párrafos'] > 1:
        resumen.append(f"Está organizado en {est['párrafos']} párrafos")
    return resumen


def analizar_texto_completo(texto):
    print("ANÁLISIS DE TEXTO")
    print("=" * 40)

    est = analizar_estructura(texto)
    for linea in generar_resumen_legible(est):
        print("-", linea)

    emails = encontrar_patrones_email(texto)
    if emails:
        print("\n📧 Emails encontrados:", emails)

    telefonos = encontrar_patrones_telefono(texto)
    if telefonos:
        print("\n📞 Teléfonos encontrados:", telefonos)

    sentimiento = analizar_sentimiento_basico(texto)
    print("\n😊 Análisis de sentimiento:", sentimiento)

    repetidas = encontrar_palabras_repetidas(texto)
    if repetidas:
        print("\n🔁 Palabras repetidas:")
        for palabra, freq in repetidas.items():
            print(f"   {palabra}: {freq} veces")


analizar = """
Hola, mi nombre es Steban y mi correo es carrizosaortegon.steban@gmail.com.
Hoy estamos joya.
Puedes llamarme al +57 321 430 66 52 o al +57 300 689 83 62.
Este es mi texto para analizar.
"""

analizar_texto_completo(analizar)