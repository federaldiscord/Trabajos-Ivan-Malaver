from collections import Counter
import heapq

class NodoHuffman:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def comprimir_repeticion_simple(texto):
    if not texto:
        return ""
    comprimido = []
    contador = 1
    for i in range(1, len(texto)):
        if texto[i] == texto[i-1]:
            contador += 1
        else:
            comprimido.append(f"{contador}{texto[i-1]}")
            contador = 1
    comprimido.append(f"{contador}{texto[-1]}")
    return "".join(comprimido)

def descomprimir_repeticion_simple(texto):
    import re
    partes = re.findall(r'(\d+)(\D)', texto)
    return "".join(int(num) * char for num, char in partes)

def construir_arbol_huffman(texto):
    frecuencias = Counter(texto)
    heap = [NodoHuffman(char, freq) for char, freq in frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        izq = heapq.heappop(heap)
        der = heapq.heappop(heap)
        nuevo = NodoHuffman(None, izq.freq + der.freq, izq, der)
        heapq.heappush(heap, nuevo)

    return heap[0]

def construir_codigos(nodo, codigo_actual="", codigos=None):
    if codigos is None:
        codigos = {}
    if nodo:
        if nodo.char is not None:
            codigos[nodo.char] = codigo_actual
        construir_codigos(nodo.left, codigo_actual + "0", codigos)
        construir_codigos(nodo.right, codigo_actual + "1", codigos)
    return codigos

def comprimir_huffman(texto):
    raiz = construir_arbol_huffman(texto)
    codigos = construir_codigos(raiz)
    texto_codificado = "".join(codigos[char] for char in texto)
    return texto_codificado, codigos

def descomprimir_huffman(texto_codificado, codigos):
    inverso = {v: k for k, v in codigos.items()}
    codigo = ""
    resultado = []
    for bit in texto_codificado:
        codigo += bit
        if codigo in inverso:
            resultado.append(inverso[codigo])
            codigo = ""
    return "".join(resultado)

if __name__ == "__main__":
    texto = "aaabbbccccccdddddaa"

    print("Texto original:", texto)
    print("\n--- RLE ---")
    comprimido_rle = comprimir_repeticion_simple(texto)
    print("Comprimido:", comprimido_rle)
    print("Descomprimido:", descomprimir_repeticion_simple(comprimido_rle))

    print("\n--- Huffman ---")
    comprimido_huffman, codigos = comprimir_huffman(texto)
    print("Códigos:", codigos)
    print("Comprimido (binario):", comprimido_huffman)
    print("Descomprimido:", descomprimir_huffman(comprimido_huffman, codigos))
