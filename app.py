import sys
from interface.interface import *
from utils.computador import Computador
from utils.processo import Processo

computador = Computador(6)



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
