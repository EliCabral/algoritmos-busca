from grafos.grafo_romenia import grafo_romenia
from grafos.grafo2 import grafo2

class ProblemaGrafo:
    def __init__(self, estado_inicial, objetivo):
        self.estado_inicial = estado_inicial
        self.objetivo_estado = objetivo
        self.grafo = grafo2


    def objetivo(self, estado):
        #print(f"estado: {estado}")
        return estado == self.objetivo_estado

    def sucessor(self, estado):
        # Retorna as transições com base no grafo
        return [(acao, vizinho) for vizinho, acao in self.grafo.get(estado, [])]



