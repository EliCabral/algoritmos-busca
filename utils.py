from grafo2 import grafo2


def reconstruir_caminho(no):
    caminho = []
    while no:
        caminho.append(no['estado'])
        no = no['pai']
    return list(reversed(caminho))


def expandir(no, problema):
    sucessores = []
    estado_atual = no['estado']
    
    for vizinho, custo in problema.grafo.get(estado_atual, []): 
        sucessores.append({
            'estado': vizinho,
            'custo': custo + no['custo'],  
            'pai': no  
        })

    return sucessores






# def expandir(no, problema, visitados):
#     sucessores = []
#     estado_atual = no['estado']
    
#     for vizinho, custo in problema.grafo.get(estado_atual, []): 
#         if vizinho not in visitados: 
#             sucessores.append({
#                 'estado': vizinho,
#                 'custo': custo + no['custo'],  
#                 'pai': no 
#             })

#     return sucessores
