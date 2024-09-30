def reconstruir_caminho(no):
    caminho = []
    while no:
        caminho.append(no['estado'])
        no = no['pai']
    return list(reversed(caminho))

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



def compara_custo(item):
    return item[0]  


def insere_fila_menor_custo(fila, item):
    fila.append(item) 
    fila.sort(key=compara_custo)  


def remove_no_menor_custo(fila):
    if len(fila) > 0:
        return fila.pop(0)  
    return None  


