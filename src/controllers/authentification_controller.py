import json

class Authentification():
    def __init__(self, storage_file: str) -> None:
        self.storage_file = storage_file

    def authenticate(code: list) -> bool:
        """
        Receives the inputed user code and validates it based on user settings
        retrieved from long term memory.  Then returns a boolean based on
        whether or not the code is considered valid.

        Args:
            code (list): _description_

        Returns:
            bool: _description_
        """
        with open('sample.json', 'r') as openfile:
            json_object = json.load(openfile)
            if json_object["2-factor"]:
                pass
            else:
                if json_object["passcode"] == code:
                    return True

    def get_key_state() -> bool:
        """when called, the getKeyState procedure uses data from the key sensor
        to determine whether the key of the Perfect Safe is inserted.

        Returns:
            bool: _description_
        """

        pass