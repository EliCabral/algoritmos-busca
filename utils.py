def reconstruir_caminho(estado_final, rastreamento_pais):
    caminho = []
    estado_atual = estado_final
    while estado_atual is not None:
        caminho.append(estado_atual)
        estado_atual = rastreamento_pais.get(tuple(estado_atual))
    return list(reversed(caminho))


# def reconstruir_caminho(no):
#     caminho = []
#     while no:
#         caminho.append(no['estado'])
#         no = no['pai']
#     return list(reversed(caminho))

def expandir(no, problema, visitados):
    sucessores = []
    estado_atual = no['estado']
    
    for vizinho, custo in problema.grafo.get(estado_atual, []): 
        if vizinho not in visitados: 
            sucessores.append({
                'estado': vizinho,
                'custo': custo + no['custo'],  
                'pai': no 
            })

    return sucessores


# def print_nos_explorados(nos_explorados):
#     print("\nNós Explorados:")
#     for no in nos_explorados:
#         estado = no['estado']
#         print_matriz(estado)


def print_caminho(caminho):
    print("Caminho da solução:")
    for i, estado in enumerate(caminho):
        print(f"Passo {i}:")
        for j in range(0, 9, 3):
            print(" ".join(str(x) for x in estado[j:j+3]))  
        print()  



def imprimir_nos_expandidos(nos_expandidos):
    print("\nNós Expandidos:")
    for index, no in enumerate(nos_expandidos):
        estado = no['estado']
        pai = no['pai']
        print(f"Passo {index}:")
        print(f"Estado: {estado}")
        if pai is not None:
            print(f"Pai: {pai}")
        print()  



def print_matriz(estado):
    for i in range(0, len(estado), 3):
        print(' '.join(map(str, estado[i:i+3])))




def movimentos_validos(indice_zero):
    acoes = {}
    
    if indice_zero % 3 != 0:  
        acoes['esquerda'] = -1
    if indice_zero % 3 != 2:
        acoes['direita'] = 1
    if indice_zero >= 3:     
        acoes['cima'] = -3
    if indice_zero < 6:  
        acoes['baixo'] = 3
    return acoes



def expandir_pecas(no, visitados):
    estado_atual = no['estado']
    indice_zero = estado_atual.index(0)  
    possiveis_movimentos = []  

    acoes = movimentos_validos(indice_zero)

    for deslocamento in acoes.values():
        novo_indice = indice_zero + deslocamento
        novo_estado = estado_atual[:]  

        novo_estado[indice_zero], novo_estado[novo_indice] = novo_estado[novo_indice], novo_estado[indice_zero]

        if tuple(novo_estado) not in visitados:
            possiveis_movimentos.append({'estado': novo_estado, 'pai': no})

    return possiveis_movimentos



