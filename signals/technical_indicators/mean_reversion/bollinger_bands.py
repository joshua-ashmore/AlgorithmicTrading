"""Bollinger bands objects."""

import pandas as pd


class BollingerBands:
    """Bollinger bands object."""

    def calculate(
        self, data: pd.Series, window_length: int = 20, standard_deviations: int = 2
    ) -> pd.Series:
        rolling = data.rolling(window_length)
        if standard_deviations == 0:
            bband = rolling.mean()
        else:
            bband = rolling.mean() + rolling.std(ddof=0) * standard_deviations
        return bband
