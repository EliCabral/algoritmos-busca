from problema_grafos import ProblemaGrafo
from busca import busca_largura, busca_custo_uniforme, busca_profundidade

def realizar_buscas():
    problema = ProblemaGrafo(estado_inicial='A', objetivo='F')
    #problema = ProblemaGrafo(estado_inicial='Arad', objetivo='Bucareste')
    
    caminho, custo = busca_largura(problema)
    print("\nBusca em largura: ")
    print('Caminho encontrado:' , ' -> '.join(caminho))
    print("Custo total:", custo)
    #450

    caminho, custo = busca_custo_uniforme(problema)
    print("\nBusca em custo uniforme: ")
    print('Caminho encontrado:' , ' -> '.join(caminho))
    print("Custo total:", custo)
    # 418

 
    caminho, custo = busca_profundidade(problema)
    print("\nBusca_profundidade: ")
    print('Caminho encontrado:' , ' -> '.join(caminho))
    print("Custo total:", custo)
    # 607

if __name__ == "__main__":
    realizar_buscas()

