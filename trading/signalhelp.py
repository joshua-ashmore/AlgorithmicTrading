"""Signal related objects."""

from typing import Optional


class Signals:
    """Trading signals object."""

    def __init__(self):
        """Init."""
        self.signal: Optional[str] = None
        self.position_held: bool = False

    def buy_entry_signal(self):
        """Buy entry signal logic - abstracted."""
        pass

    def sell_entry_signal(self):
        """Sell entry signal logic - abstracted."""
        pass

    def buy_exit_signal(self):
        """Buy exit signal logic - abstracted."""
        pass

    def sell_exit_signal(self):
        """Sell exit signal logic - abstracted."""
        pass
