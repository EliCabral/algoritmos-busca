from utils import reconstruir_caminho, expandir

def BPL(problema, no, limite, visitados, borda_final):
    estado_atual = no['estado']
    
    visitados.add(estado_atual)

    if problema.objetivo(estado_atual):
        return reconstruir_caminho(no), no['custo']

    if limite > 0:
        sucessores = expandir(no, problema, visitados)
        
        for sucessor in sucessores:
            borda_final.add(sucessor['estado'])
        
        print(f"Borda: {[sucessor['estado'] for sucessor in reversed(sucessores)]}")
        
        resultado_final = 'CORTE'  
        melhor_custo = None

        for sucessor in sucessores:
            resultado, custo = BPL(problema, sucessor, limite - 1, visitados, borda_final)
            if resultado != 'CORTE':
                return resultado, custo  
            else:
                resultado_final = 'CORTE'  

        return resultado_final, melhor_custo 
    else:
        return 'CORTE', None 


def busca_profundidade_limitada(problema, limite):
    print("\nBusca em profundidade limitada\n")
    
    no_inicial = {'estado': problema.estado_inicial, 'custo': 0, 'pai': None}
    visitados = set()  
    borda_final = set()  

    resultado, custo = BPL(problema, no_inicial, limite, visitados, borda_final)

    if resultado != 'CORTE':
        print(f"\nNós explorados: {len(visitados)}") 
        print(f"Quantidade de nós na borda final: {len(borda_final)}")  

        return resultado, custo  
    else:
        print(f"\nTotal de nós explorados: {len(visitados)}")
        return [], 'sem resultados'
