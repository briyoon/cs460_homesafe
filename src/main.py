import sys
import json
import os

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from widgets import Handle, KeyHole, KeyPad


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        screen = QApplication.primaryScreen()

        screen_width = screen.size().width()
        screen_height = screen.size().height()
        app_width = int(screen.size().width() / 1.2)
        app_height = int(screen.size().height() / 1.2)

        # self.setGeometry(
        #     (screen_width - app_width) // 2,
        #     (screen_height - app_height) // 2,
        #     app_width,
        #     app_height
        # )
        self.setWindowTitle("Perfect Safe")

        # initialize safe_storage.json if needed
        storage_path = "resources/settings.json"
        if not os.path.isfile(storage_path):
            with open(storage_path, 'w') as outfile:
                defaults = {
                    "passcode": "1234",
                    "two_factor": False,
                    "volume": 2
                }
                json_object = json.dumps(defaults, indent=4)
                outfile.write(json_object)

        # layout
        centralWidget = QWidget()
        layout = QtWidgets.QHBoxLayout()

        # init widgets
        self.handle = Handle()
        self.keyhole = KeyHole()
        self.keypad = KeyPad()

        # add widgets
        layout.addWidget(self.handle)
        layout.addWidget(self.keyhole)
        layout.addWidget(self.keypad)

        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)


if __name__ == "__main__":
    if sys.version_info.major != 3 or sys.version_info.minor < 10:
        sys.exit("Please use Python version 3.10 or above")
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())