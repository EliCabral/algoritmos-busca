import heapq
from utils import expandir_pecas, imprimir_nos_expandidos, print_caminho, reconstruir_caminho

def busca_a_star(problema):
    print("\nBusca A*")
    
    fila_prioridade = [] 
    custo_caminho_atual = 0 
    custo_heuristico_inicial = problema.heuristica(problema.estado_inicial, problema.estado_objetivo)
    
    heapq.heappush(fila_prioridade, (custo_heuristico_inicial, problema.estado_inicial, custo_caminho_atual, None))  
    
    estados_visitados = set()  
    caminho_solucao = []  
    total_nos_expandidos = 0  
    rastreamento_pais = {}

    while fila_prioridade:
        custo_heuristico_atual, estado_atual, custo_caminho_atual, pai = heapq.heappop(fila_prioridade)

        if tuple(estado_atual) in estados_visitados:
            continue

        rastreamento_pais[tuple(estado_atual)] = pai
        estados_visitados.add(tuple(estado_atual))
        total_nos_expandidos += 1

        if problema.objetivo(estado_atual):
            print("\nSolução encontrada!")
            caminho_solucao = reconstruir_caminho(estado_atual, rastreamento_pais)  
            print_caminho(caminho_solucao)  
            print(f"Nós expandidos: {total_nos_expandidos}")  
            print(f"Nós na borda final: {len(fila_prioridade)}") 
            return caminho_solucao  

        sucessores = expandir_pecas({'estado': estado_atual, 'pai': pai}, estados_visitados)

        for sucessor in sucessores:
            custo_caminho_sucessor = custo_caminho_atual + 1  
            custo_heuristico_sucessor = problema.heuristica(sucessor['estado'], problema.estado_objetivo)
            custo_total_sucessor = custo_caminho_sucessor + custo_heuristico_sucessor  

            if tuple(sucessor['estado']) not in estados_visitados:
                heapq.heappush(fila_prioridade, (custo_total_sucessor, sucessor['estado'], custo_caminho_sucessor, estado_atual))

    print("Nenhuma solução encontrada.")
    return [], 'sem resultados'


