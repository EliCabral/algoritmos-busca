from grafos.problema_grafos import ProblemaGrafo
from buscas.busca_largura import busca_largura
from buscas.busca_custo_uniforme import busca_custo_uniforme
from buscas.busca_profundidade import busca_profundidade
from buscas.busca_profundidade_limitada import busca_profundidade_limitada

def realizar_buscas():
    problema = ProblemaGrafo(estado_inicial='A', objetivo='F')
    #problema = ProblemaGrafo(estado_inicial='Arad', objetivo='Bucareste')
    
    caminho, custo = busca_largura(problema)
    print('\nCaminho encontrado:' , ' -> '.join(caminho))
    print("Custo total:", custo)
    print("\n########################################################################")
    #450


    caminho, custo = busca_custo_uniforme(problema)
    print('\nCaminho encontrado:' , ' -> '.join(caminho))
    print("Custo total:", custo)
    print("\n########################################################################")
    # 418

 
    caminho, custo = busca_profundidade(problema)
    print('\nCaminho encontrado:' , ' -> '.join(caminho))
    print("Custo total:", custo)
    print("\n########################################################################")
    # 607

    caminho, custo = busca_profundidade_limitada(problema, 4)
    print('\nCaminho encontrado:' , ' -> '.join(caminho))
    print("Custo total:", custo)

if __name__ == "__main__":
    realizar_buscas()
