import os
from enum import Enum
import playsound


class sounds(Enum):
    SHORT = "resources/shortbeep.wav"
    LONG = "resources/longbeep.wav"

class colors(Enum):
    RED = "RED"

def play_tone(volume: int, tone: sounds) -> bool:
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
        playsound.playsound(tone.value, False)
        return True
    except:
        print("failed to play sound")
        return False

def led_feedback(length: int, color: colors) -> bool:
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
        # playsound.playsound("resources/shortbeep.wav")
        return True
    except:
        return False
