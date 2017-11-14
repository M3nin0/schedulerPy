from utils.fila import *

class Computador():
    def __init__(self, quantum_limit):
        self.quantum_limit = quantum_limit
        self.fila_circular = FilaCircular(3, 4, 7)
        self.fila_batch = FilaCircular(1, 4, 5)

    def insere_processo(self, processo):
        if processo.tipo == 'sistema':
            pass
        if processo.tipo == 'circular':
            self.fila_circular.add_processo(processo)
        else:
            self.fila_batch.add_processo(processo)

    def executa_processos(self, sistema, interativa, circular):
        if sistema.count() > 0:
            pass
        if interativa.count() > 0:
            self.fila_circular.run()
        if circular > 0:
            self.fila_circular.run()
