def heuristica_manhattan(estado_atual, estado_objetivo):
    distancia = 0
    for i in range(len(estado_atual)):
        if estado_atual[i] != 0:  
            posicao_correta = estado_objetivo.index(estado_atual[i])
            distancia += abs(i // 3 - posicao_correta // 3) + abs(i % 3 - posicao_correta % 3)
    return distancia
