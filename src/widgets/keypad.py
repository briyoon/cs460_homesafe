from PyQt6 import QtWidgets
from controllers import keypad_controller
from models import Odin

class KeyPad(QtWidgets.QFrame):
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
        button.clicked.connect(self.pound_it)
        layout.addWidget(button)
        self._buttons.append(button)

        self.setLayout(layout)

        with open("./src/widgets/keypad.css") as f:
            self.setStyleSheet(f.read())

    def pound_it(self) -> None:
        state = Odin.keypad_state
        if state == Odin.KeypadState.IDLE:
            keypad_controller.enter_code()
        if state == Odin.KeypadState.PASSCODE_REQUEST:
            keypad_controller.command_access()
        if state == Odin.KeypadState.ENTER_NEW_PASS:
            keypad_controller.new_pass()
        if state == Odin.KeypadState.CONFIRM_NEW_PASS:
            keypad_controller.confirm_new_pass()
        Odin.current_code = ""

