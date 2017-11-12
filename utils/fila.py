'''
Classe que representa o escalonamento circular
'''

# Cores dos estágios do processo
# Executando: #2ecc71
# Pronto: #3498db
# Em espera: #f39c12

from utils.processo import Processo
from time import sleep

class Circular():
    def __init__(self, prioridade, qtd_processos, tempo_limite):
        self._prioridade = prioridade
        self.fila = {}
        self._total = 0
        self.qtd_processos = qtd_processos
        # Tempo limite de cada execução
        self.tempo_limite = tempo_limite
        self.cores = {'executando': '#2ecc71', 'pronto': '#3498db', 'espera': '#f39c12'}

    @property
    def prioridade(self):
        return self._prioridade

    def add(self, processo):
        # self.fila.append(processo)
        self.fila[processo.id] = processo

    def remove(self, processo):
        # self.fila.remove(processo)
        del self.fila[processo.id]

    def run(self, label):
        while len(self.fila) != 0:
            for p in range(0, len(self.fila)):
                c = 0
                print('Processo sendo executado: ID ' + str(self.fila[p].id))
                while c < self.tempo_limite:
                    sleep(2)
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
        self._prioridade = prioridade
        self.fila = {}
        self._total = 0
        self.qtd_processos = qtd_processos
        # Tempo limite de cada execução
        self.tempo_limite = tempo_limite
        self.cores = {'executando': '#2ecc71', 'pronto': '#3498db', 'espera': '#f39c12'}

    @property
    def prioridade(self):
        return self._prioridade

    def add(self, processo):
        # self.fila.append(processo)
        self.fila[processo.id] = processo

    def remove(self, processo):
        # self.fila.remove(processo)
        del self.fila[processo.id]

    def run(self, label):
        pass
