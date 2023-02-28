from PyQt6 import QtWidgets
from controllers import keypad_controller

class KeyPad(QtWidgets.QWidget):
    """
    Custom Qt Widget to show the keypad
    """

    def __init__(self, *args, **kwargs):
        super(KeyPad, self).__init__(*args, **kwargs)

        self.initGUI()

    def initGUI(self):
        layout = QtWidgets.QGridLayout()
        self._buttons: list(QtWidgets.QPushButton) = []
        for i in range(9):
            button = QtWidgets.QPushButton()
            button.setText(str(i + 1))
            button.clicked.connect(lambda _, digit=i + 1: keypad_controller.input_char(str(digit)))
            layout.addWidget(button, i // 3, i % 3)
            self._buttons.append(button)

        button = QtWidgets.QPushButton()
        button.setText('*')
        button.clicked.connect(lambda: keypad_controller.input_char('*'))
        layout.addWidget(button)
        self._buttons.append(button)

        button = QtWidgets.QPushButton()
        button.setText('0')
        button.clicked.connect(lambda: keypad_controller.input_char('0'))
        layout.addWidget(button)
        self._buttons.append(button)

        button = QtWidgets.QPushButton()
        button.setText('#')
        button.clicked.connect(keypad_controller.enter_code)
        layout.addWidget(button)
        self._buttons.append(button)

        self.setLayout(layout)
