from utils.fila import *
from utils.processo import Processo
from PyQt5.QtWidgets import QInputDialog

class Computador():
    def __init__(self, quantum_limit, window):
        self.quantum_limit = quantum_limit
        self.fila_interativo = FilaCircular(3, 4, 7, window)
        self.fila_batch = FilaCircular(1, 4, 5, window)
        self.window = window
        self.ids = 0

    def __get_info(self):
        tempo, ok = QInputDialog.getInt(self.window, 'Tempo', 'Insira o tempo de execução do processo')
        prioridade, ok = QInputDialog.getInt(self.window, 'Prioridade', 'Insira a prioridade do processo')
        return tempo, prioridade

    def insere_processo(self, tipo):
        self.ids += 1
        if tipo == 'sistema':
            pass
        if tipo == 'interativo':
            tempo, prioridade = self.__get_info()
            self.fila_interativo.add_processo(Processo(self.ids, tempo * 2, prioridade, ), 'interativo')
        else:
            tempo, prioridade = self.__get_info()
            self.fila_batch.add_processo(Processo(self.ids, tempo, prioridade), 'sistema')

    def executa_processos(self):
        if self.window.fila_sistema.count() > 0:
            pass
        if self.window.fila_interativa.count() > 0:
            self.fila_interativo.ini('interativo', self.quantum_limit)
        if self.window.fila_batch.count() > 0:
            self.fila_batch.ini('batch', self.quantum_limit)
