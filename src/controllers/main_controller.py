from controllers import storage_controller as sc
from controllers.storage_controller import Settings
from controllers import output_controller as oc
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
            oc.led_feedback(0.25, "green")
            print("Volume set to 0")
        case "*991":
            sc.write_file(Settings.VOLUME, 1)
            Odin.keypad_state = Odin.KeypadState.IDLE
            oc.led_feedback(0.25, "green")
            print("Volume set to 1")
        case "*992":
            sc.write_file(Settings.VOLUME, 2)
            Odin.keypad_state = Odin.KeypadState.IDLE
            oc.led_feedback(0.25, "green")
            print("Volume set to 2")
        case "*111":
            sc.write_file(Settings.TWO_FACTOR, False)
            oc.led_feedback(0.25, "green")
            Odin.keypad_state = Odin.KeypadState.IDLE
        case "*222":
            sc.write_file(Settings.TWO_FACTOR, True)
            oc.led_feedback(0.25, "green")
            Odin.keypad_state = Odin.KeypadState.IDLE
        case "*456":
            oc.led_feedback(0.25, "green")
            Odin.keypad_state = Odin.KeypadState.ENTER_NEW_PASS
        case _: # deafult (invalid)
            print("Invalid command")
            oc.led_feedback(0.25, "red")
            Odin.keypad_state = Odin.KeypadState.IDLE