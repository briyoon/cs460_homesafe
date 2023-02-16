from PyQt6 import QtWidgets, QtGui
import os


class KeyHole(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super(KeyHole, self).__init__(*args, **kwargs)

        self.keystate: bool = False

        self.initGUI()

    def initGUI(self):
        self.setIcon(QtGui.QIcon("resources/key_empty.png"))
        self.clicked.connect(self.toggle_keystate)

    def toggle_keystate(self):
        self.keystate = not self.keystate
        icon_path = "key_inserted" if self.keystate else "key_empty"
        icon_path = "resources/" + icon_path + ".png"
        print(icon_path)
        self.setIcon(QtGui.QIcon(icon_path))
