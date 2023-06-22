"""Moving average convergence divergence file."""

import pandas as pd


class MACD:
    """Moving average convergence divergence object."""

    def calculate(
        self,
        data: pd.Series,
        short_window_length: int = 12,
        long_window_length: int = 26,
        smooth_window_length: int = 9,
    ):
        """Calculate MACD."""
        fast_ema = data.ewm(span=short_window_length, adjust=False).mean()
        slow_ema = data.ewm(span=long_window_length, adjust=False).mean()
        macd = pd.Series(slow_ema - fast_ema)
        signal = macd.ewm(span=smooth_window_length, adjust=False).mean()
        return signal
