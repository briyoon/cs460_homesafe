from controllers import SafeConfig


class Odin():
    """
    Singleton object that tracks state for the entire safe
    """
    password: str
    current_code: str

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Odin, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # list state
        self.password: str = "1234"
        self.current_code: str = ""