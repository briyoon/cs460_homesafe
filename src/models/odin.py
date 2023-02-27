class Odin():
    """
    Singleton object that tracks state for the entire safe
    """
    current_code: str = ""

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Odin, cls).__new__(cls)
        return cls.instance

    # def __init__(self):
    #     # list state
    #     self.current_code: str = ""