from enum import Enum

# from widgets import handle


class Odin():
    """
    Singleton object that tracks state for the entire safe
    """

    class KeypadState(Enum):
        IDLE = 0
        PASSCODE_REQUEST = 1
        ENTER_NEW_PASS = 5
        CONFIRM_NEW_PASS = 6

    storage_path: str = "resources/settings.json"
    current_code: str = ""
    key_state: bool = False
    door_open: bool = False
    keypad_state: KeypadState = KeypadState.IDLE
    command: str = ""
    thors_handle = None
    keypad = None


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Odin, cls).__new__(cls)
        return cls.instance

    # def __init__(self):
    #     # list state
    #     self.current_code: str = ""