import os
from enum import Enum
import playsound


class sounds(Enum):
    SHORT = "resources/shortbeep.wav"
    LONG = "resources/longbeep.wav"

class colors(Enum):
    RED = "RED"

def play_tone(volume: int, tone: sounds) -> bool:
    try:
        playsound.playsound(tone.value, False)
        return True
    except:
        print("failed to play sound")
        return False

def led_feedback(length: int, color: colors) -> bool:
    try:
        # playsound.playsound("resources/shortbeep.wav")
        return True
    except:
        return False
