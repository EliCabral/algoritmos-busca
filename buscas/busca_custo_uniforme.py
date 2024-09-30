from utils import insere_fila_menor_custo, remove_no_menor_custo, reconstruir_caminho, expandir
import heapq 

def busca_custo_uniforme(problema):
    print("\nBusca em custo uniforme\n")

    fila = []  
    heapq.heappush(fila, (0, {'estado': problema.estado_inicial, 'custo': 0, 'pai': None}))    
    visitados = set() 
    custos = {problema.estado_inicial: 0} 
    count = 0

    while fila:
        count += 1
        print(count, "º Borda:", [no['estado'] for _, no in fila])
        # print(f"{count}º Borda:", [no['estado'] for _, no in fila])

        custo_atual, no = heapq.heappop(fila)  

        estado_atual = no['estado']

        if estado_atual in visitados:
            continue  # pula os visitados

        visitados.add(estado_atual)

        if problema.objetivo(estado_atual):
            print(f"\nNós explorados: {count}")
            print(f"Quantidade de nós na borda final: {len(fila)}")
            return reconstruir_caminho(no), custo_atual  #objetivo alcançado, retorna caminho

        sucessores = expandir(no, problema, visitados)

        for sucessor in sucessores:
            if sucessor['estado'] not in visitados:
                custo_total = sucessor['custo']  
                
                if (sucessor['estado'] not in custos) or (custo_total < custos[sucessor['estado']]):
                    custos[sucessor['estado']] = custo_total 
                    heapq.heappush(fila, (custo_total, sucessor)) 

    return [], 'sem resultados'  

