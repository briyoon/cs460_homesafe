from controllers import storage_controller as sc
from controllers.storage_controller import Settings

def handle_command(command: str):
    """
    Upon receiving the command from the Authentication object, this procedure
    will be called with the received command as the parameter. The actual
    procedure that's executed will depend on which command was received from the
    Authentication object.

    Args:
        command (int): _description_
    """
    match command:
        case "*990":
            sc.write_file(Settings.VOLUME, 0)
        case "*991":
            sc.write_file(Settings.VOLUME, 1)
        case "*992":
            sc.write_file(Settings.VOLUME, 2)
        case "*111":
            sc.write_file(Settings.TWO_FACTOR, False)
        case "*222":
            sc.write_file(Settings.TWO_FACTOR, True)
        case "*456":
            pass
        case _: # deafult (invalid)
            print("Invalid command")