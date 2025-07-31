import random

def rolar_dados(lados, vezes):
    resultado = []
    for _ in range(vezes):
        resultado.append(random.randint(1, lados))
    return resultado

print(rolar_dados(6, 5))