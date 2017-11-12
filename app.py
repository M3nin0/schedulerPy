# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils.fila import Circular
from utils.processo import Processo

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(QWidget):

    # Executando: #2ecc71
    # Pronto: #3498db
    # Em espera: #f39c12

    def get_info(self):
        id, ok = QInputDialog.getInt(self, 'ID', 'Insira o ID do processo')
        tempo, ok = QInputDialog.getInt(self, 'Tempo', 'Insira o tempo de execução do processo')
        prioridade, ok = QInputDialog.getInt(self, 'Prioridade', 'Insira a prioridade do processo')

        return id, tempo, prioridade

    def add_processo_sistema(self):

        id, tempo, prioridade = self.get_info()

        item = QtWidgets.QListWidgetItem('Processo ' + str(id))
        item.setBackground(QColor('#3498db'))
        self.fila_sistema.addItem(item)
        # self.circular.add(Processo(id, tempo, prioridade))

    def add_processo_interativo(self):
        id, tempo, prioridade = self.get_info()

        item = QtWidgets.QListWidgetItem('Processo ' + str(id))
        item.setBackground(QColor('#3498db'))
        self.fila_interativa.addItem(item)
        self.interativo.add(Processo(id, tempo, prioridade))

    def add_processo_batch(self):

        id, tempo, prioridade = self.get_info()

        item = QtWidgets.QListWidgetItem('Processo ' + str(id))
        item.setBackground(QColor('#3498db'))
        self.fila_batch.addItem(item)
        self.batch.add(Processo(id, tempo, prioridade))

    def setupUi(self, MainWindow):

        self.interativo = Circular(3, 4, 10)
        self.batch = Circular(1, 4, 13)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_executa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_executa.setGeometry(QtCore.QRect(20, 320, 141, 71))
        self.btn_executa.setObjectName("pushButton")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(50, 80, 768, 192))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.fila_sistema = QtWidgets.QListWidget(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fila_sistema.setFont(font)
        self.fila_sistema.setObjectName("fila_sistema")

        self.fila_interativa = QtWidgets.QListWidget(self.splitter)
        self.fila_interativa.setObjectName("fila_interativa")

        self.fila_batch = QtWidgets.QListWidget(self.splitter)
        self.fila_batch.setObjectName("fila_batch")

        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(50, 40, 771, 29))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")

        self.btn_sistema = QtWidgets.QPushButton(self.splitter_2)
        self.btn_sistema.setObjectName("btn_sistema")
        self.btn_sistema.clicked.connect(self.add_processo_sistema)

        self.btn_batch = QtWidgets.QPushButton(self.splitter_2)
        self.btn_batch.setObjectName("btn_batch")

        self.btn_interativo = QtWidgets.QPushButton(self.splitter_2)
        self.btn_interativo.setObjectName("btn_interativo")
        self.btn_interativo.clicked.connect(self.add_processo_interativo)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 23))
        self.menubar.setObjectName("menubar")
        self.menuInicio = QtWidgets.QMenu(self.menubar)
        self.menuInicio.setObjectName("menuInicio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.menuInicio.addAction(self.actionSobre)
        self.menubar.addAction(self.menuInicio.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multiplas filas"))
        self.btn_executa.setText(_translate("MainWindow", "Iniciar processador"))
        self.btn_sistema.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_sistema.setText(_translate("MainWindow", "Adicionar processo de sistema"))
        self.btn_batch.setText(_translate("MainWindow", "Adicionar processo batch"))
        self.btn_interativo.setText(_translate("MainWindow", "Adicionar processo interativo"))
        self.menuInicio.setTitle(_translate("MainWindow", "Inicio"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
