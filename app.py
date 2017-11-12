# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils.fila import Circular
from utils.fila import Prioridade
from utils.processo import Processo

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(QWidget):

    def executa_processos(self):

        if self.fila_sistema.count() > 0:
            self.prioridade.run(self.fila_sistema)

        if self.fila_interativa.count() > 0:
            self.interativo.run(self.fila_interativa)

        if self.fila_batch.count() > 0:
            self.batch.run(self.fila_batch)

        # item = self.fila_batch.item(0)
        # item.setBackground(QColor('#2ecc71'))
        # item.setBackground(QColor('#2ecc71'))
        # self.fila_batch.takeItem(0)

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

        self.prioridade = Prioridade(5, 4, 11)
        self.interativo = Circular(3, 4, 10)
        self.batch = Circular(1, 4, 9)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 490)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_executa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_executa.setGeometry(QtCore.QRect(20, 330, 141, 71))
        self.btn_executa.setObjectName("pushButton")
        self.btn_executa.clicked.connect(self.executa_processos)


        self.lbl_pronto_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pronto_2.setGeometry(QtCore.QRect(720, 310, 95, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_pronto_2.setFont(font)
        self.lbl_pronto_2.setStyleSheet("")
        self.lbl_pronto_2.setObjectName("lbl_pronto_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(50, 40, 751, 29))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.btn_sistema = QtWidgets.QPushButton(self.splitter)
        self.btn_sistema.setObjectName("btn_sistema")
        self.btn_sistema.clicked.connect(self.add_processo_sistema)

        self.btn_interativo = QtWidgets.QPushButton(self.splitter)
        self.btn_interativo.setObjectName("btn_interativo")
        self.btn_interativo.clicked.connect(self.add_processo_interativo)

        self.btn_batch = QtWidgets.QPushButton(self.splitter)
        self.btn_batch.setObjectName("btn_batch")
        self.btn_batch.clicked.connect(self.add_processo_batch)

        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(60, 80, 768, 192))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.fila_sistema = QtWidgets.QListWidget(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fila_sistema.setFont(font)
        self.fila_sistema.setObjectName("fila_sistema")
        self.fila_interativa = QtWidgets.QListWidget(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.fila_interativa.setFont(font)
        self.fila_interativa.setObjectName("fila_interativa")
        self.fila_batch = QtWidgets.QListWidget(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.fila_batch.setFont(font)
        self.fila_batch.setObjectName("fila_batch")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(710, 340, 95, 72))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.lbl_pronto = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_pronto.setFont(font)
        self.lbl_pronto.setStyleSheet("background-color: rgb(52, 152, 219);")
        self.lbl_pronto.setObjectName("lbl_pronto")
        self.lbl_espera = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_espera.setFont(font)
        self.lbl_espera.setStyleSheet("background-color: rgb(243, 156, 18);")
        self.lbl_espera.setTextFormat(QtCore.Qt.RichText)
        self.lbl_espera.setObjectName("lbl_espera")
        self.lbl_executando = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_executando.setFont(font)
        self.lbl_executando.setStyleSheet("background-color: rgb(46, 204, 113);")
        self.lbl_executando.setObjectName("lbl_executando")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multiplas filas"))
        self.btn_executa.setText(_translate("MainWindow", "Iniciar processador"))
        self.lbl_pronto_2.setText(_translate("MainWindow", "Legenda"))
        self.btn_sistema.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.btn_sistema.setText(_translate("MainWindow", "Adicionar processo de sistema"))
        self.btn_interativo.setText(_translate("MainWindow", "Adicionar processo interativo"))
        self.btn_batch.setText(_translate("MainWindow", "Adicionar processo batch"))
        self.lbl_pronto.setText(_translate("MainWindow", "Pronto"))
        self.lbl_espera.setText(_translate("MainWindow", "Em espera"))
        self.lbl_executando.setText(_translate("MainWindow", "Executando"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
