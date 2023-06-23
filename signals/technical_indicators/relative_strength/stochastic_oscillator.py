"""Stochastic oscillator object."""

import pandas as pd
from utils.assertions import items_of_sublist_in_list


class StochasticOscillator:
    """Stochastic osciallator object."""

    def calculate(self, data: pd.DataFrame, window_length: int = 14) -> pd.DataFrame:
        """Calculate stochastic oscillator signal."""
        assert items_of_sublist_in_list(
            sublist=["High", "Low", "Close"], parent_list=data.columns
        )
        high_roll = data["High"].rolling(window_length).max()
        low_roll = data["Low"].rolling(window_length).min()

        # Fast stochastic indicator
        num = data["Close"] - low_roll
        denom = high_roll - low_roll
        stochastic_oscillator_df = pd.DataFrame()
        stochastic_oscillator_df["%K"] = (num / denom) * 100

        # Slow stochastic indicator
        stochastic_oscillator_df["%D"] = (
            stochastic_oscillator_df["%K"].rolling(3).mean()
        )

        return stochastic_oscillator_df
