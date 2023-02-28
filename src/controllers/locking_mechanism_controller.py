from models import Odin

def get_current_state() -> bool:
    """
    uses data from the door sensor to determine whether the door of the Perfect
    Safe is currently closed or open, where true would correspond to open and
    false to closed.

    Returns:
        bool: _description_
    """
    pass

def open_safe() -> None:
    Odin.door_open = True

def close_safe() -> None:
    Odin.door_open = False