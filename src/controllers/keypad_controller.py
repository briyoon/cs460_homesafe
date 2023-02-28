from models import Odin
from controllers import main_controller, output_controller, storage_controller, \
    authentification_controller, locking_mechanism_controller

def input_char(input: str) -> None:
    """
    Receives user key presses returning each character individually to the main
    processor.

    Args:
        input (str): _description_
    """
    output_controller.play_tone(output_controller.sounds.SHORT)
    if len(Odin.current_code) < 12:
        Odin.current_code += input
    print(Odin.current_code)

def enter_code() -> None:
    code = Odin.current_code
    Odin.current_code = ""

    output_controller.play_tone(output_controller.sounds.SHORT)
    if(authentification_controller.authenticate(code)):
        if code[0] == '*':
            main_controller.handle_command(code)
        else:
            # locking_mechanism_controller.open_safe() # open safe
            pass
    else:
        # error beep
        ...
