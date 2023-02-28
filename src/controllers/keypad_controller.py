from models import Odin
from controllers import main_controller, output_controller, storage_controller

def input_char(input: str) -> None:
    """
    Receives user key presses returning each character individually to the main
    processor.

    Args:
        input (str): _description_
    """
    output_controller.play_tone(7, output_controller.sounds.SHORT)
    if len(Odin.current_code) < 12:
        Odin.current_code += input
    print(Odin.current_code)

def enter_code() -> None:
    output_controller.play_tone(output_controller.sounds.SHORT)
    main_controller.handle_command(Odin.current_code)
