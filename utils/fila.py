import numpy as np
from time import sleep
from utils.processo import Processo
from PyQt5.QtGui import QColor
from PyQt5 import QtWidgets

class Fila():
    def __init__(self, prioridade, qtd_processos, window):
        self.prioridade = prioridade
        self.qtd_processos = qtd_processos
        self.fila = np.ndarray(qtd_processos, Processo)
        self.fila[0] = Processo(); self.fila[1] = Processo()
        self.fila[2] = Processo(); self.fila[3] = Processo()
        self.window = window
        self.total = 0
        self.cores = {'executando': '#2ecc71', 'pronto': '#3498db', 'espera': '#f39c12'}

    def is_full(self):
        return self.total == self.qtd_processos

    def is_empty(self):
        return self.total == 0

    def add_processo(self, processo, tipo):
        if not self.is_full():
            new_item = QtWidgets.QListWidgetItem('Processo ' + str(processo.id) + '\nPrioridade ' + str(processo.prioridade))
            new_item.setBackground(QColor('#3498db'))

            if tipo == 'sistema':
                self.window.fila_sistema.insertItem(self.total, new_item)
            if tipo == 'interativo':
                self.window.fila_interativa.insertItem(self.total, new_item)
            if tipo == 'batch':
                self.window.fila_batch.insertItem(self.total, new_item)

            self.fila[self.total] = processo
            self.total += 1

class FilaCircular(Fila):
    def __init__(self, prioridade, qtd_processos, window):
        super(FilaCircular, self).__init__(prioridade, qtd_processos, window)
        self.primeiro = 0
        self.ultimo = 0

    def add_processo(self, processo, tipo):
        if not self.is_full():
            new_item = QtWidgets.QListWidgetItem('Processo ' + str(processo.id) + '\nPrioridade ' + str(processo.prioridade))
            new_item.setBackground(QColor('#3498db'))
            if tipo == 'sistema':
                self.window.fila_sistema.insertItem(self.total, new_item)
            if tipo == 'interativo':
                self.window.fila_interativa.insertItem(self.total, new_item)
            if tipo == 'batch':
                self.window.fila_batch.insertItem(self.total, new_item)

            self.fila[self.ultimo] = processo
            self.ultimo = (self.ultimo + 1) % len(self.fila)
            self.total += 1

    def remove_processo(self):
        if not self.is_empty():
            temp = self.fila[self.primeiro]
            self.primeiro = (self.primeiro + 1) % len(self.fila)
            self.total -= 1

    def ini(self, tipo, quantum_limit):

        if tipo == 'interativo':
            actual_fila = self.window.fila_interativa
        elif tipo == 'batch':
            actual_fila = self.window.fila_batch
        elif tipo == 'sistema':
            actual_fila = self.window.fila_sistema

        total = 0
        while total < len(self.fila):
            for i in range(0, self.total):

                actual_item = actual_fila.item(0)

                try:
                    actual_item.setBackground(QColor(self.cores['executando']))
                    # self.window.fila_interativa.hide()
                    # self.window.fila_interativa.show()
                    # actual_fila.update()
                    # self.window.fila_interativa.update()
                except:
                    total += 1
                    continue

                c = 0
                while c < quantum_limit:
                    self.fila[i].tempo_de_execucao -= 1
                    sleep(1)
                    c += 1

                if self.fila[i].tempo_de_execucao < 0:
                    actual_fila.takeItem(0)
                    total += 1
                else:
                    actual_fila.takeItem(0)
                    actual_fila.insertItem(self.total, actual_item)

                # self.window.actual_fila.hide()
                # self.window.actual_fila.show()
                # actual_fila.update()
                # self.window.update()

        for i in range(0, len(self.fila)):
            self.remove_processo()

class FilaPrioridade(Fila):
    def __init__(self, prioridade, qtd_processos, window):
        super(FilaPrioridade, self).__init__(prioridade, qtd_processos, window)

    def ini(self, quantum_limit):

        self.fila.sort()

        print(int(str(self.fila[0])))

        for i in range(0, self.total):
            actual_item = self.window.fila_sistema.item(int(str(self.fila[i])))

            # actual_item.setBackground(QColor(self.cores['executando']))
            # try:
            #     actual_item.setBackground(QColor(self.cores['executando']))
            # except:
            #     print('Erro')
            #     continue

            while self.fila[i].tempo_de_execucao > 0:
                sleep(2)
                self.fila[i].tempo_de_execucao -= 1

            self.window.fila_sistema.takeItem(int(str(self.fila[i])))
