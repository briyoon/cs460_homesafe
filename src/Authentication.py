import json

class Authentification():
    def __init__(self, storage_file:str) -> None:
        self.storage_file = storage_file

    def authenticate(code:list) -> bool:
        with open('sample.json', 'r') as openfile:
            json_object = json.load(openfile)
            if json_object["2-factor"]:
                pass
            else:
                if json_object["passcode"] == code:
                    return True