from collections import deque
from utils import reconstruir_caminho, expandir

def busca_largura(problema):
    print("\nBusca em largura\n")

    fila = deque() 
    fila.append({'estado': problema.estado_inicial, 'pai': None, 'custo': 0}) 
    count = 0
    visitados = set() 

    while fila:
        count+=1
        print(f"{count}º Borda:", [no['estado'] for no in fila])

        no = fila.popleft() 

        if no['estado'] in visitados:
            continue  

        visitados.add(no['estado'])

        if problema.objetivo(no['estado']):
            print(f"\nNós explorados: {count}")
            print(f"Quantidade de nós na borda final: {len(fila)}")
            return reconstruir_caminho(no), no['custo']  #objetivo alcançado, retorna caminho e custo

        sucessores = expandir(no, problema, visitados)
        for s in sucessores:
            if s['estado'] not in visitados and s not in fila:  
                fila.append(s)  # adicionando os sucessores nao visitados

    return [], 'sem resultados'   
