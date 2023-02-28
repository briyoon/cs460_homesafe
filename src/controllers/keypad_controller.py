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
    print(f"Keystate: {Odin.key_state}")
    print(f"You entered: {code}")
    output_controller.play_tone(output_controller.sounds.SHORT)

    if len(code) > 0 and code[0] == '*':
        Odin.command = code
        Odin.keypad_state = Odin.KeypadState.PASSCODE_REQUEST
    else:
        if authentification_controller.authenticate(code):
            print("open!!!!")
            locking_mechanism_controller.open_safe()

def command_access():
    if authentification_controller.authenticate(Odin.current_code):
        main_controller.handle_command(Odin.command)

def new_pass():
    if not Odin.current_code[0] == "*":
        Odin.keypad_state = Odin.KeypadState.CONFIRM_NEW_PASS
        Odin.command = Odin.current_code
    else:
        Odin.keypad_state = Odin.KeypadState.IDLE

def confirm_new_pass():
    if Odin.current_code == Odin.command:
        storage_controller.write_file(storage_controller.Settings.PASSWORD, Odin.current_code)
    Odin.keypad_state = Odin.KeypadState.IDLE
