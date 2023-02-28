from enum import Enum
from pygame import mixer

import threading

from models import Odin
from controllers import storage_controller


class sounds(Enum):
    SHORT = "resources/shortbeep.wav"
    LONG = "resources/longbeep.wav"

class colors(Enum):
    RED = "RED"

def play_tone(tone: sounds) -> bool:
    """
    Receives a signal from the output controller determining the volume at which
    the buzzer should tone and for how long.  Returns a boolean that the signal
    was processed properly.

    Args:
        volume (int): _description_
        tone (sounds): _description_

    Returns:
        bool: _description_
    """
    try:
        volume = storage_controller.read_file(storage_controller.Settings.VOLUME)
        match volume:
            case 2:
                volume = 1
            case 1:
                volume = 0.5
            case 0:
                volume = 0
            case _:
                print("err")
        mixer.music.load(tone.value)
        mixer.music.set_volume(volume)
        mixer.music.play()
        # playsound.playsound(tone.value, False)
        return True
    except:
        print("failed to play sound")
        return False

def led_feedback(length: int, color: str) -> bool:
    """
    Receives a signal from the output controller determining the color of LED
    that should be lit and for how long.  Returns a boolean that the signal was
    processed properly.

    Args:
        length (int): _description_
        color (colors): _description_

    Returns:
        bool: _description_
    """

    try:
        thread = threading.Thread(target=Odin.keypad.blink, args=(color, length))
        thread.start()
        return True
    except:
        return False
