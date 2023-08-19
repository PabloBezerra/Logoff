from PyQt6 import uic, QtWidgets, QtGui
import os
from time import sleep

app = QtWidgets.QApplication([])

janela1 = uic.loadUi('Sucesso.ui')
janela1.show()

app.exec()