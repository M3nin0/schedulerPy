import numpy as np
from utils.processo import Processo

class Fila():
    def __init__(self, prioridade, qtd_processos, quantum):
        self.prioridade = prioridade
        self.qtd_processos = qtd_processos
        self.quantum = quantum
        self.fila = np.ndarray(qtd_processos, Processo)

class FilaCircular(Fila):
    def __init__(self, prioridade, qtd_processos, quantum):
        super(FilaCircular, self).__init__(prioridade, qtd_processos, quantum)
        self.primeiro = 0
        self.total = 0
        self.ultimo = 0

    def is_full(self):
        return self.total == self.qtd_processos

    def is_empty(self):
        return self.total == 0

    def add_processo(self, processo):
        if not self.is_full():
            self.fila[self.ultimo] = processo
            self.ultimo = (self.ultimo + 1) % len(self.fila)
            self.total += 1

    def remove_processo(self):
        if not self.is_empty():
            temp = self.fila[self.primeiro]
            self.primeiro = (self.primeiro + 1) % len(self.fila)
            self.total -= 1
            return temp

    def ini():
        pass
