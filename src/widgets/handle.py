from PyQt6 import QtWidgets, QtCore, QtGui

from models import Odin


class Handle(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super(Handle, self).__init__(*args, **kwargs)
        self.initGUI()

    def initGUI(self):
        self.setIcon(QtGui.QIcon("resources/handle_closed.png"))
        self.clicked.connect(self.close_door)

        self.setFixedSize(100, 100)
        self.setIconSize(QtCore.QSize(100, 100))

        with open("./src/widgets/handle.css") as f:
            self.setStyleSheet(f.read())

    def close_door(self):
        if Odin.door_open:
            self.toggle_door_state()

    def toggle_door_state(self):
        if Odin.door_open:
            Odin.door_open = False
            self.setIcon(QtGui.QIcon("resources/handle_closed.png"))
            return

        self.setIcon(QtGui.QIcon("resources/handle_open.png"))


