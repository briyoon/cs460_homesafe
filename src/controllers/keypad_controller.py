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

    if len(code) > 0 and code[0] == '*':
        Odin.command = code
        print("Command read")
        output_controller.led_feedback(0.25, "green")
        Odin.keypad_state = Odin.KeypadState.PASSCODE_REQUEST
    else:
        if authentification_controller.authenticate(code):
            print("OPEN!!!!")
            output_controller.led_feedback(0.5, "green")
            Odin.thors_handle.open_door()
            locking_mechanism_controller.open_safe()
        else:
            print("Failed")
            output_controller.led_feedback(0.25, "red")
        

def command_access():
    if authentification_controller.authenticate(Odin.current_code):
        output_controller.led_feedback(0.25, "green")
        main_controller.handle_command(Odin.command)
        print("Command applied")
    else:
        Odin.keypad_state = Odin.KeypadState.IDLE

def new_pass():
    if not Odin.current_code[0] == "*":
        Odin.keypad_state = Odin.KeypadState.CONFIRM_NEW_PASS
        output_controller.led_feedback(0.25, "green")
        Odin.command = Odin.current_code
        print("New Passcode Valid")
    else:
        Odin.keypad_state = Odin.KeypadState.IDLE
        output_controller.led_feedback(0.25, "red")
        print("Invalid Passcode")

def confirm_new_pass():
    if Odin.current_code == Odin.command:
        storage_controller.write_file(storage_controller.Settings.PASSWORD, Odin.current_code)
        output_controller.led_feedback(0.25, "green")
        print("Passcode Changed")
    else:
        output_controller.led_feedback(0.25, "red")
        print("NP CHANGE")
    Odin.keypad_state = Odin.KeypadState.IDLE
