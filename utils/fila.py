'''
Classe que representa o escalonamento circular
'''

from utils.processo import Processo
from time import sleep

class Circular():
    def __init__(self, prioridade, qtd_processos, tempo_limite):
        self.prioridade = prioridade
        self.qtd_processos = qtd_processos
        # Tempo limite de cada execução
        self.tempo_limite = tempo_limite
        self.fila = []

    def add(self, processo):
        self.fila.append(processo)

    def remove(self, processo):
        self.fila.remove(processo)

    def run(self):
        while len(self.fila) != 0:
            for p in range(0, len(self.fila)):
                c = 0
                print('Processo sendo executado: ID ' + str(self.fila[p].id))
                while c < self.tempo_limite:
                    sleep(1)
                    self.fila[p].tempo -= 1
                    c += 1
                if self.fila[p].tempo <= 0:
                    print('Processo finalizado: ID ' + str(self.fila[p].id))
                    self.fila.remove(self.fila[p])
                else:
                    print('Processo entrou em espera: ID ' + str(self.fila[p].id))
                    temp = self.fila[p]
                    self.fila.remove(self.fila[p])
                    self.fila.append(temp)

class Prioridade():
    def __init__(self, prioridade, qtd_processos, tempo_limite):
        pass
