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
        if texto[i] == texto[i - 1]:
            contador += 1
        else:
            comprimido.append(f"{contador}{texto[i - 1]}")
            contador = 1
    comprimido.append(f"{contador}{texto[-1]}")
    return ''.join(comprimido)

def descomprimir_repeticion_simple(texto):
    if not texto:
        return ""
    descomprimido = []
    i = 0
    while i < len(texto):
        count = 0
        while i < len(texto) and texto[i].isdigit():
            count = count * 10 + int(texto[i])
            i += 1
        if i < len(texto):
            descomprimido.append(texto[i] * count)
            i += 1
    return ''.join(descomprimido)
