import sys

from PyQt5.uic import *
from PyQt5.QtGui import *
from utils.processo import Processo
from utils.computador import Computador
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QPushButton, QAction, QInputDialog


app = QApplication(sys.argv)
window = loadUi('./interface/view.ui')

computador = Computador(6, window)

# Adicionando ações aos botões
window.btn_sistema.clicked.connect(lambda: computador.insere_processo('sistema'))
window.btn_interativo.clicked.connect(lambda: computador.insere_processo('interativo'))
window.btn_batch.clicked.connect(lambda: computador.insere_processo('batch'))
window.pushButton.clicked.connect(lambda: computador.executa_processos())


if __name__ == '__main__':

    window.show()
    sys.exit(app.exec_())
