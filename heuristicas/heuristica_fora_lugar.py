def heuristica_foras_do_lugar(estado, objetivo):
    contador = 0 
    for i in range(len(estado)):
        if estado[i] != 0 and estado[i] != objetivo[i]:
            contador += 1  
    return contador