from utils import reconstruir_caminho, expandir

# def busca_profundidade(problema):
#     print("\nBusca em profundidade\n")
#     pilha = [{'estado': problema.estado_inicial, 'custo': 0, 'pai': None}]
#     visitados = set()
#     contador_nos = 0 

#     while pilha:
#         no = pilha.pop() 

#         estado_atual = no['estado']

#         if estado_atual in visitados:
#             continue  # pula os visitados

#         visitados.add(estado_atual)

#         contador_nos += 1

#         if problema.objetivo(estado_atual):
#             print(f"\nNós explorados: {contador_nos}")
#             print(f"Quantidade de nós na borda final: {len(pilha)}")
#             return reconstruir_caminho(no), no['custo']  #objetivo alcançado, retorna caminho e custo


#         sucessores = expandir(no, problema, visitados)
        
#         # usando reversed para a ordem correta
#         for sucessor in reversed(sucessores):
#             if sucessor['estado'] not in visitados:
#                 pilha.append(sucessor)   # adicionando os sucessores nao visitados

#         print(f"Borda atual: {[n['estado'] for n in pilha]}") 
    
#     return [], 'sem resultados'  



def busca_profundidade(problema):
    print("\nBusca em profundidade\n")
    pilha = [{'estado': problema.estado_inicial, 'custo': 0, 'pai': None}]
    visitados = set()
    contador_nos = 0 

    while pilha:


        no = pilha.pop() 

        estado_atual = no['estado']

        if estado_atual in visitados:
            continue  # pula os visitados

        visitados.add(estado_atual)

        contador_nos += 1

        #                 # Antes de checar o objetivo, imprima a borda atual
        # print(f"Borda atual: {[n['estado'] for n in pilha]}") 
        
        if problema.objetivo(estado_atual):
            print(f"\nNós explorados: {contador_nos}")
            # Imprima a borda final após encontrar o objetivo
            print(f"Quantidade de nós na borda final: {len(pilha)}")
            return reconstruir_caminho(no), no['custo']  # objetivo alcançado, retorna caminho e custo

        sucessores = expandir(no, problema, visitados)

        # usando reversed para a ordem correta
        for sucessor in reversed(sucessores):
            if sucessor['estado'] not in visitados:
                pilha.append(sucessor)  # adicionando os sucessores não visitados

        print(f"Borda atual: {[n['estado'] for n in pilha]}")

    return [], 'sem resultados'
