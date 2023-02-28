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
    print(Odin.key_state)
    output_controller.play_tone(output_controller.sounds.SHORT)

    if len(code) > 0 and code[0] == '*':
        command = code
        passcode = request_code()
        if authentification_controller.authenticate(passcode):
            main_controller.handle_command(command)
    else:
        if authentification_controller.authenticate(code):
            locking_mechanism_controller.open_safe()

def request_code():
    ...