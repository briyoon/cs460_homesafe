from PyQt6 import QtWidgets
import asyncio
import time
from qasync import asyncSlot
import threading

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
        layout = QtWidgets.QVBoxLayout()
        keypad_layout = QtWidgets.QGridLayout()
        led_layout = QtWidgets.QHBoxLayout()
        self._buttons: list(QtWidgets.QPushButton) = []

        # self._loop = asyncio.get_event_loop()
        self._loop = asyncio.get_event_loop()

        self._red_led = QtWidgets.QFrame()
        self._green_led = QtWidgets.QFrame()
        self._red_led.setProperty("cssClass", "led")
        self._green_led.setProperty("cssClass", "led")

        led_layout.addWidget(self._red_led)
        led_layout.addWidget(self._green_led)

        for i in range(9):
            button = QtWidgets.QPushButton()
            button.setText(str(i + 1))
            button.clicked.connect(lambda _, digit=i + 1: keypad_controller.input_char(str(digit)))
            keypad_layout.addWidget(button, i // 3, i % 3)
            self._buttons.append(button)

        button = QtWidgets.QPushButton()
        button.setText('*')
        button.clicked.connect(lambda: keypad_controller.input_char('*'))
        # button.clicked.connect(lambda: self.create_led_thread("green", 2))
        keypad_layout.addWidget(button)
        self._buttons.append(button)

        button = QtWidgets.QPushButton()
        button.setText('0')
        button.clicked.connect(lambda: keypad_controller.input_char('0'))
        keypad_layout.addWidget(button)
        self._buttons.append(button)

        button = QtWidgets.QPushButton()
        button.setText('#')
        button.clicked.connect(self.pound_it)
        keypad_layout.addWidget(button)
        self._buttons.append(button)

        layout.addLayout(led_layout)
        layout.addLayout(keypad_layout)

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
        print(Odin.keypad_state)

    def create_led_thread(self, type, duration):
        thread = threading.Thread(target=self.blink, args=(type, duration))
        thread.start()

    def blink(self, type: str, duration: int):
        if type == "red":
            self._red_led.setStyleSheet("background-color: red;")
            time.sleep(duration)
            self._red_led.setStyleSheet("background-color: black;")
        elif type == "green":
            self._green_led.setStyleSheet("background-color: green;")
            time.sleep(duration)
            self._green_led.setStyleSheet("background-color: black;")


