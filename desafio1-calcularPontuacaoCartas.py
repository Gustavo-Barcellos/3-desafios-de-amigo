mao = [5, 3, 10, 2]
pontuacao = 0

def calcular_Puntuacao():
    global pontuacao
    pontuacao += sum(mao)
    print (pontuacao)

calcular_Puntuacao()