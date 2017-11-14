from PyQt5.uic import *
from PyQt5.QtGui import *
from utils.fila import *
from utils.processo import Processo
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QPushButton, QAction, QInputDialog

class Computador():
    def __init__(self, quantum_limit, window):
        self.quantum_limit = quantum_limit
        self.fila_interativo = FilaCircular(3, 4, 7)
        self.fila_batch = FilaCircular(1, 4, 5)
        self.window = window
        self.ids = 0
        self.cores = {'executando': '#2ecc71', 'pronto': '#3498db', 'espera': '#f39c12'}

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
            self.fila_interativo.add_processo(Processo(self.ids, tempo, prioridade))
        else:
            tempo, prioridade = self.__get_info()
            self.fila_batch.add_processo(Processo(self.ids, tempo, prioridade))

    def executa_processos(self, sistema, interativa, circular):
        if sistema.count() > 0:
            pass
        if interativa.count() > 0:
            self.fila_circular.ini()
        if circular > 0:
            self.fila_circular.ini()
