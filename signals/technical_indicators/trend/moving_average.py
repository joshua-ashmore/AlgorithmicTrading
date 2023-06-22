"""Moving average technical indicator object."""

import pandas as pd
from typing import Union
from static_data.enums import MovingAverageTypes


class MovingAverage:
    """Moving average object."""

    def calculate(
        self,
        data: Union[pd.DataFrame, pd.Series],
        moving_average_type: MovingAverageTypes,
        window_length: int = 14,
    ):
        """Calculate moving average."""
        if moving_average_type == "SMA":
            return data.rolling(window=window_length).mean()
        elif moving_average_type == "EMA":
            return data.ewm(span=window_length).mean()
