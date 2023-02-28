from enum import Enum
import json
import traceback

from models import Odin


class Settings(Enum):
    PASSWORD = "passcode"
    TWO_FACTOR = "two_factor"
    VOLUME = "volume"


def read_file(setting: Settings) -> str | int | Exception:
    """
    Receives a string from the storage setting controller as to which setting
    needs to be pulled from memory. Returns the current value of the setting
    parameter or Error if no such parameter exists.

    Args:
        setting (Settings): _description_

    Returns:
        str | int: _description_
    """
    try:
        with open(Odin.storage_path, "r") as f:
            settings_file = json.load(f)
            return settings_file[setting.value]
    except:
        traceback.print_exc()
        print("error reading json")
        return Exception

def write_file(setting:Settings, new_value:str|int|bool) -> bool:
    """
    Receives a string from the storage setting controller as to which setting
    needs to be changed and the new value to replace the setting with.
    Returns a boolean based on whether the parameter being written to exists.

    Args:
        setting (Settings): _description_
        new_value (str): _description_

    Returns:
        bool: _description_
    """
    try:
        with open(Odin.storage_path, "r") as f:
            settings_file = json.load(f)
        settings_file[setting.value] = new_value
        with open(Odin.storage_path, "w") as f:
            json.dump(settings_file, f)
        return True
    except:
        traceback.print_exc()
        print("error writing reading json")
        return False
