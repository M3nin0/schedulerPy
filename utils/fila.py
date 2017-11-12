'''
Classe que representa o escalonamento circular
'''

# Cores dos estágios do processo
# Executando: #2ecc71
# Pronto: #3498db
# Em espera: #f39c12

from time import sleep
from PyQt5.QtGui import *
from utils.processo import Processo

class Circular():
    def __init__(self, prioridade, qtd_processos, quantum):
        self._prioridade = prioridade
        self.fila = []
        self._total = 0
        self.qtd_processos = qtd_processos
        # Tempo limite de cada execução
        self.quantum = quantum
        self.cores = {'executando': '#2ecc71', 'pronto': '#3498db', 'espera': '#f39c12'}

    def refresh(self,lista):
        lista.update()
        lista.repaint()

    @property
    def prioridade(self):
        return self._prioridade

    def add(self, processo):
        self.fila.append(processo)
        # self.fila[processo.id] = processo

    def remove(self, processo, lista):
        lista.takeItem(0)
        self.fila.remove(processo)
        self.refresh(lista)
        # del self.fila[processo.id]

        # item = self.fila_batch.item(1)
        # item.setBackground(QColor('#2ecc71'))

        # self.fila_batch.takeItem(0)

    def run(self, lista):
        while len(self.fila) != 0:
            for p in range(0, len(self.fila)):
                c = 0

                item = lista.item(0)
                item.setBackground(QColor(self.cores['executando']))
                lista.insertItem(0, item)
                self.refresh(lista)

                while c < self.quantum:
                    print('Rodando: ' + str(self.fila[p].id))
                    sleep(1)
                    self.fila[p].tempo -= 1
                    c += 1
                if self.fila[p].tempo <= 0:
                    print('Terminado')
                    self.remove(self.fila[p], lista)
                else:
                    print('Parando: ' + str(self.fila[p].id))
                    lista.takeItem(0)
                    item.setBackground(QColor(self.cores['pronto']))
                    lista.addItem(item)
                    self.refresh(lista)
                    temp = self.fila[p]
                    self.fila.remove(self.fila[p])
                    self.fila.append(temp)

class Prioridade():
    def __init__(self, prioridade, qtd_processos, quantum):
        self._prioridade = prioridade
        self.fila = []
        self._total = 0
        self.qtd_processos = qtd_processos
        # Tempo limite de cada execução
        self.quantum = quantum
        self.cores = {'executando': '#2ecc71', 'pronto': '#3498db', 'espera': '#f39c12'}

    def refresh(self,lista):
        lista.update()
        lista.repaint()

    @property
    def prioridade(self):
        return self._prioridade

    def add(self, processo):
        self.fila.append(processo)
        # self.fila[processo.id] = processo

    def remove(self, processo, lista):
        lista.takeItem(0)
        self.fila.remove(processo)
        self.refresh(lista)
