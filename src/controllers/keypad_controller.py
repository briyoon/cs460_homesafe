from models import Odin
from controllers import main_controller, output_controller

def input_char(input: str) -> None:
    output_controller.play_tone()
    if len(Odin.current_code) < 12:
        Odin.current_code += input
    print(Odin.current_code)