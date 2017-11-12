'''
Classe que representa o escalonamento circular
'''

from time import sleep
from escalonador import processo

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
            for processo in self.fila:
                c = 0
                print('Processo sendo executado: ID ' + str(processo.id))
                while (c < self.tempo_limite):
                    sleep(1)
                    processo.tempo -= 1
                    c += 1
                if processo.tempo <= 0:
                    print('Processo finalizado: ID ' + str(processo.id))
                    self.remove(processo)
                else:
                    print('Processo entrou em espera: ID ' + str(processo.id))
        print('Todos os processos foram executados')
