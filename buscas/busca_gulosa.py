import heapq

from utils import expandir_pecas, print_caminho, reconstruir_caminho


def busca_gulosa(problema):
    print("\nBusca Gulosa")

    fila = []  
    heuristica_inicial = problema.heuristica(problema.estado_inicial, problema.estado_objetivo)
    heapq.heappush(fila, (heuristica_inicial, problema.estado_inicial, None))  
    visitados = set()  
    rastreamento_pais = {}  
    nos_expandidos = 0  

    while fila:
        heuristica_atual, estado_atual, pai = heapq.heappop(fila)

        if tuple(estado_atual) in visitados:
            continue

        rastreamento_pais[tuple(estado_atual)] = pai

        visitados.add(tuple(estado_atual))
        nos_expandidos += 1 

        if problema.objetivo(estado_atual):
            print("\nSolução encontrada!")
            caminho = reconstruir_caminho(estado_atual, rastreamento_pais)  
            print_caminho(caminho)
            print(f"Nós expandidos: {nos_expandidos}")  
            print(f"Nós na borda final: {len(fila)}")  
            return caminho

        sucessores = expandir_pecas({'estado': estado_atual, 'pai': pai}, visitados)

        for sucessor in sucessores:
            heuristica_sucessor = problema.heuristica(sucessor['estado'], problema.estado_objetivo)
            if tuple(sucessor['estado']) not in visitados:
                heapq.heappush(fila, (heuristica_sucessor, sucessor['estado'], estado_atual))
    

    print("Nenhuma solução encontrada.")
    return [], 'sem resultados'