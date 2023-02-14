from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import QtWidgets

import sys

from widgets import KeyPad

app = QApplication(sys.argv)

window = QMainWindow()
centralWidget = QWidget()
layout = QtWidgets.QVBoxLayout()

keypad = KeyPad()

layout.addWidget(keypad)
centralWidget.setLayout(layout)
window.setCentralWidget(centralWidget)
window.show()

app.exec()