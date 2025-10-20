def es_primo_simple(numero):
    if numero < 2:
        return False

    print(f"Verificando si {numero} es primo:")
    for i in range(2, int(numero ** 0.5) + 1):
        print(f"  ¿{numero} es divisible por {i}? ", end="")
        if numero % i == 0:
            print(f"Sí ({numero} / {i} = {numero // i})")
            return False
        else:
            print("No")
    print(f"✔ {numero} es primo")
    return True


def criba_eratostenes(limite):
    print(f"Aplicando Criba de Eratóstenes hasta {limite}")
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False

    print(f"Lista inicial: {es_primo[:min(20, len(es_primo))]}...")
    for i in range(2, int(limite ** 0.5) + 1):
        if es_primo[i]:
            print(f"\nMarcando múltiplos de {i}:")
            for j in range(i * i, limite + 1, i):
                if es_primo[j]:
                    print(f"  {j} (múltiplo de {i}) → No primo")
                    es_primo[j] = False
    primos = [i for i in range(2, limite + 1) if es_primo[i]]
    return primos


def factorizacion_prima(numero):
    print(f"\nFactorización prima de {numero}:")
    factores = []
    divisor = 2
    numero_temp = numero

    while divisor * divisor <= numero_temp:
        while numero_temp % divisor == 0:
            factores.append(divisor)
            print(f"  {numero_temp} ÷ {divisor} = {numero_temp // divisor}")
            numero_temp //= divisor
        divisor += 1

    if numero_temp > 1:
        factores.append(numero_temp)
        print(f"  Factor primo final: {numero_temp}")

    return factores


print("GENERADOR DE NÚMEROS PRIMOS")
print("=" * 40)

numeros_probar = [17, 25, 29]
print("1. VERIFICACIÓN INDIVIDUAL:")
for num in numeros_probar:
    resultado = es_primo_simple(num)
    print()

print("\n2. CRIBA DE ERATÓSTENES:")
print("-" * 30)
primos_hasta_30 = criba_eratostenes(30)
print(f"\nPrimos encontrados hasta 30: {primos_hasta_30}")
print(f"Total de primos: {len(primos_hasta_30)}")

print("\n3. FACTORIZACIÓN PRIMA:")
print("-" * 30)
numero_factorizar = 60
factores = factorizacion_prima(numero_factorizar)
factores_str = " × ".join(map(str, factores))
print(f"\n{numero_factorizar} = {factores_str}")

producto = 1
for factor in factores:
    producto *= factor
print(f"Verificación: {factores_str} = {producto}")