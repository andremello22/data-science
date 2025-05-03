"""programação orientada a objetos"""

def crivo(numero):
    primos = [True] *(numero + 1)
    primos[0] = False
    primos[1] = False

    for i in range(2, int(numero**0.5)+1):

        if primos[i]:
            for j in range(i*i, numero +1, i):
                primos[j] = False

    return [primo for primo, valor in enumerate(primos) if valor]

print(crivo(100))