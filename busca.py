from collections import deque
import heapq
from utils import reconstruir_caminho, expandir

from collections import deque

def busca_largura(problema):
    fila = deque() 
    fila.append({'estado': problema.estado_inicial, 'pai': None, 'custo': 0}) 

    visitados = set() 

    while fila:
        no = fila.popleft() 

        if no['estado'] in visitados:
            continue  

        visitados.add(no['estado'])

        if problema.objetivo(no['estado']):
            return reconstruir_caminho(no), no['custo']  #objetivo alcançado, retorna caminho e custo

        sucessores = expandir(no, problema)
        for s in sucessores:
            if s['estado'] not in visitados:  
                fila.append(s)  # adicionando os sucessores nao visitados
                print(f"fila de sucessores: {fila}")

    return [], 'sem resultados'   


def busca_custo_uniforme(problema):
    fila = []  
    heapq.heappush(fila, (0, {'estado': problema.estado_inicial, 'custo': 0, 'pai': None}))  
    visitados = set() 
    custos = {problema.estado_inicial: 0}  

    while fila:
        custo_atual, no = heapq.heappop(fila)  

        estado_atual = no['estado']

        if estado_atual in visitados:
            continue  # pula os visitados

        visitados.add(estado_atual)

        if problema.objetivo(estado_atual):
            return reconstruir_caminho(no), custo_atual  #objetivo alcançado, retorna caminho

        sucessores = expandir(no, problema)

        for sucessor in sucessores:
            if sucessor['estado'] not in visitados:
                custo_total = sucessor['custo']  
                
                if (sucessor['estado'] not in custos) or (custo_total < custos[sucessor['estado']]):
                    custos[sucessor['estado']] = custo_total 
                    heapq.heappush(fila, (custo_total, sucessor)) 

    return [], 'sem resultados'  



def busca_profundidade(problema):
    pilha = [{'estado': problema.estado_inicial, 'custo': 0, 'pai': None}]
    visitados = set()

    while pilha:
        no = pilha.pop() 

        estado_atual = no['estado']

        if estado_atual in visitados:
            continue  # pula os visitados

        visitados.add(estado_atual)

        if problema.objetivo(estado_atual):
            return reconstruir_caminho(no), no['custo']  #objetivo alcançado, retorna caminho e custo

        sucessores = expandir(no, problema)
        
        # usando reversed para a ordem correta
        for sucessor in reversed(sucessores):
            if sucessor['estado'] not in visitados:
                pilha.append(sucessor)   # adicionando os sucessores nao visitados

    return [], 'sem resultados'  






