def handle_command(command: int):
    """
    Upon receiving the command from the Authentication object, this procedure
    will be called with the received command as the parameter. The actual
    procedure that's executed will depend on which command was received from the
    Authentication object.

    Args:
        command (int): _description_
    """
    match command:

        case _: # deafult (invalid)
            pass