from enum import Enum
import playsound

class sounds(Enum):
    SHORT = "resources/shortbeep.wav"
    LONG = "resources/longbeep.wav"

class colors(Enum):
    RED = "RED"

def play_tone(volume: int, type: sounds) -> bool:
    try:
        playsound.playsound("resources/shortbeep.wav")
        return True
    except:
        return False

def led_feedback(length: int, color: colors) -> bool:
    try:
        # playsound.playsound("resources/shortbeep.wav")
        return True
    except:
        return False
