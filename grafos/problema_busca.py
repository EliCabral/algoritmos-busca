from grafos.grafo_romenia import grafo_romenia
from grafos.grafo2 import grafo2

class ProblemaBusca:
    def __init__(self, estado_inicial, objetivo, heuristica):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = objetivo
        #self.grafo = grafo2  
        self.heuristica = heuristica

    # def __repr__(self):
    #     return f"ProblemaDeBusca(estado_inicial={self.estado_inicial}, estado_objetivo={self.estado_objetivo})"


    def objetivo(self, estado):
        #print(f"estado: {estado}")
        return estado == self.estado_objetivo

    # def sucessor(self, estado):
    #     return [(acao, vizinho) for vizinho, acao in self.grafo.get(estado, [])]



