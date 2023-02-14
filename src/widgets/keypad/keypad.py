from PyQt6 import QtWidgets


class KeyPad(QtWidgets.QWidget):
    """
    Custom Qt Widget to show the keypad
    """

    def __init__(self, *args, **kwargs):
        super(KeyPad, self).__init__(*args, **kwargs)

        layout = QtWidgets.QGridLayout()
        self._buttons = []
        for i in range(9):
            button = QtWidgets.QPushButton()
            button.setText(str(i))
            layout.addWidget(button, i // 3, i % 3)
            self._buttons.append(button)
        button = QtWidgets.QPushButton()
        button.setText('#')
        layout.addWidget(button)
        self._buttons.append(button)
        button = QtWidgets.QPushButton()
        button.setText('0')
        layout.addWidget(button)
        self._buttons.append(button)
        button = QtWidgets.QPushButton()
        button.setText('*')
        layout.addWidget(button)
        self._buttons.append(button)

        self.setLayout(layout)
