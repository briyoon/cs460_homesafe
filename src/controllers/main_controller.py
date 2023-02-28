from controllers import storage_controller as sc
from controllers.storage_controller import Settings
from models import Odin

def handle_command(command: str):
    """
    Upon receiving the command from the Authentication object, this procedure
    will be called with the received command as the parameter. The actual
    procedure that's executed will depend on which command was received from the
    Authentication object.

    Args:
        command (int): _description_
    """
    match command:
        case "*990":
            sc.write_file(Settings.VOLUME, 0)
            Odin.keypad_state = Odin.KeypadState.IDLE
            print("Volume set to 0")
        case "*991":
            sc.write_file(Settings.VOLUME, 1)
            Odin.keypad_state = Odin.KeypadState.IDLE
            print("Volume set to 1")
        case "*992":
            sc.write_file(Settings.VOLUME, 2)
            Odin.keypad_state = Odin.KeypadState.IDLE
            print("Volume set to 2")
        case "*111":
            sc.write_file(Settings.TWO_FACTOR, False)
            Odin.keypad_state = Odin.KeypadState.IDLE
        case "*222":
            sc.write_file(Settings.TWO_FACTOR, True)
            Odin.keypad_state = Odin.KeypadState.IDLE
        case "*456":
            Odin.keypad_state = Odin.KeypadState.ENTER_NEW_PASS
        case _: # deafult (invalid)
            print("Invalid command")