from utils.fila import *
from utils.processo import Processo
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtWidgets

class Computador():
    def __init__(self, quantum_limit, window):
        self.quantum_limit = quantum_limit
        self.fila_sistema = FilaPrioridade(5, 4, window)
        self.fila_interativo = FilaCircular(3, 4, window)
        self.fila_batch = FilaCircular(1, 4, window)
        self.window = window
        self.ids = 0

    def __get_info(self):
        tempo, ok = QInputDialog.getInt(self.window, 'Tempo', 'Insira o tempo de execução do processo')
        prioridade, ok = QInputDialog.getInt(self.window, 'Prioridade', 'Insira a prioridade do processo')
        return tempo, prioridade

    def insere_processo(self, tipo):
        self.ids += 1
        if tipo == 'sistema':
            tempo, prioridade = self.__get_info()
            self.fila_sistema.add_processo(Processo(self.ids, tempo * 2, prioridade, ), 'sistema')
        if tipo == 'interativo':
            tempo, prioridade = self.__get_info()
            self.fila_interativo.add_processo(Processo(self.ids, tempo * 2, prioridade, ), 'interativo')
        if tipo == 'batch':
            tempo, prioridade = self.__get_info()
            self.fila_batch.add_processo(Processo(self.ids, tempo, prioridade), 'batch')

        # maior = self.window.fila_sistema.item(0)
        # for i in range(0, self.window.fila_sistema.count()):
        #     if maior < self.window.fila_sistema.item(i):
        #         antigo = maior
        #         maior = self.window.fila_sistema.item(i)
        #         self.window.fila_sistema.insertItem(0, maior)
        #         self.window.fila_sistema.insertItem(i, antigo)

        self.window.fila_sistema.sortItems(order = 1)

    def executa_processos(self):
        if self.window.fila_sistema.count() > 0:
            self.fila_sistema.ini(self.quantum_limit)
        if self.window.fila_interativa.count() > 0:
            self.fila_interativo.ini('interativo', self.quantum_limit)
        if self.window.fila_batch.count() > 0:
            self.fila_batch.ini('batch', self.quantum_limit)
