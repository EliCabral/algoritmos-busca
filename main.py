from buscas.busca_gulosa import busca_gulosa
from buscas.busca_a_estrela import busca_a_star
from grafos.problema_busca import ProblemaBusca
from heuristicas.heuristica_manhattan import heuristica_manhattan
from heuristicas.heuristica_fora_lugar import heuristica_foras_do_lugar


def entrada_estado_inicial():
    while True:
        entrada = input("Digite o estado inicial, separados por espaço): ")
        estado_inicial = list(map(int, entrada.split()))

        if len(set(estado_inicial)) == 9 and all(0 <= num <= 8 for num in estado_inicial):
            return estado_inicial
        else:
            print("Estado inicial inválido. Tente novamente.")

def realizar_buscas():
    # problema = ProblemaGrafo(estado_inicial='A', objetivo='F')
    
    # caminho, custo = busca_largura(problema)
    # print('\nCaminho encontrado:' , ' -> '.join(caminho))
    # print("Custo total:", custo)
    # print("\n########################################################################")

    estado_inicial = entrada_estado_inicial()
    estado_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    print("\nEscolha a busca:")
    print("1. Busca Gulosa")
    print("2. Busca A*")
    
    escolha_busca = input("Digite 1 ou 2: ")
    
    print("\nEscolha a heurística:")
    print("1. Heurística de Manhattan")
    print("2. Heurística de peças fora do lugar")
    
    escolha_heuristica = input("Digite 1 ou 2: ")

    if escolha_heuristica == '1':
        heuristica = heuristica_manhattan
    else:
        heuristica = heuristica_foras_do_lugar

    problema = ProblemaBusca(estado_inicial, estado_objetivo, heuristica)

    if escolha_busca == '1':
        caminho = busca_gulosa(problema)
    else:
        caminho = busca_a_star(problema)

    if caminho: 
        print("Caminho encontrado")
    else:
        print("Nenhum caminho encontrado.")

if __name__ == "__main__":
    realizar_buscas()
