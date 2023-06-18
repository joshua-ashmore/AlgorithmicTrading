"""IBKR data objects."""


class Bar:
    open = 0
    close = 0
    high = 0
    low = 0
    volume = 0
    date = ""

    def __init__(self):
        """Init function."""
        self.open = 0
        self.close = 0
        self.high = 0
        self.low = 0
        self.volume = 0
        self.date = ""
