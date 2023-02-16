from PyQt6 import QtWidgets


class KeyPad(QtWidgets.QWidget):
    """
    Custom Qt Widget to show the keypad
    """

    def __init__(self, *args, **kwargs):
        super(KeyPad, self).__init__(*args, **kwargs)

        self.password: str = "1234"
        self.current_code: str = ""

        self.initGUI()

    def initGUI(self):
        layout = QtWidgets.QGridLayout()
        self._buttons: list(QtWidgets.QPushButton) = []
        for i in range(9):
            button = QtWidgets.QPushButton()
            button.setText(str(i + 1))
            button.clicked.connect(lambda _, digit=i + 1: self.enter_digit(str(digit)))
            layout.addWidget(button, i // 3, i % 3)
            self._buttons.append(button)

        button = QtWidgets.QPushButton()
        button.setText('*')
        layout.addWidget(button)
        self._buttons.append(button)

        button = QtWidgets.QPushButton()
        button.setText('0')
        button.clicked.connect(lambda: self.enter_digit('0'))
        layout.addWidget(button)
        self._buttons.append(button)

        button = QtWidgets.QPushButton()
        button.setText('#')
        button.clicked.connect(self.enter_code)
        layout.addWidget(button)
        self._buttons.append(button)

        self.setLayout(layout)

    def enter_digit(self, digit: str) -> None:
        if len(self.current_code) < 12:
            self.current_code += digit
        print(self.current_code)

    def enter_code(self) -> bool:
        retval = False
        if self.current_code == self.password:
            retval = True
        self.current_code = ""
        print(retval)
        return retval
