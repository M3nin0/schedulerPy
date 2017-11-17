import sys

from PyQt5.uic import *
from PyQt5.QtGui import *
from PyQt5.QtWebKit import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
from utils.processo import Processo
from utils.computador import Computador
from PyQt5.QtCore import QObject, pyqtSignal

app = QApplication(sys.argv)
window = loadUi('./interface/view.ui')
stack_html = open('./interface/stack.html').read()

# Configurando os QWidgets
fila_sistema = QVBoxLayout()
fila_interativa = QVBoxLayout()
fila_batch = QVBoxLayout()
window.fila_sistema.setLayout(fila_sistema)
window.fila_interativa.setLayout(fila_interativa)
window.fila_batch.setLayout(fila_batch)

# Adicionando página html no qt
view_1 = QWebView()
view_2 = QWebView()
view_3 = QWebView()

view_1.setHtml(stack_html)
view_2.setHtml(stack_html)
view_3.setHtml(stack_html)

# Adicionando viewer a interface
fila_sistema.addWidget(view_1)
fila_interativa.addWidget(view_2)
fila_batch.addWidget(view_3)

computador = Computador(6, window)

frame = view_1.page().mainFrame()

# Adicionando ações aos botões
# window.btn_sistema.clicked.connect(lambda: computador.insere_processo('sistema'))
# window.btn_interativo.clicked.connect(lambda: computador.insere_processo('interativo'))
# window.btn_batch.clicked.connect(lambda: computador.insere_processo('batch'))
window.pushButton.clicked.connect(lambda: frame.evaluateJavaScript('addSistema();'))

if __name__ == '__main__':

    window.show()
    sys.exit(app.exec_())
