from models import Odin

import storage_controller

def authenticate(code: list) -> bool:
    """
    Receives the inputed user code and validates it based on user settings
    retrieved from long term memory.  Then returns a boolean based on
    whether or not the code is considered valid.

    Args:
        code (list): _description_

    Returns:
        bool: _description_
    """
    if storage_controller.read_file(storage_controller.Settings.TWO_FACTOR):
        pass
    else:
        pass

def get_key_state() -> bool:
    """when called, the getKeyState procedure uses data from the key sensor
    to determine whether the key of the Perfect Safe is inserted.

    Returns:
        bool: _description_
    """
    return Odin.key_state