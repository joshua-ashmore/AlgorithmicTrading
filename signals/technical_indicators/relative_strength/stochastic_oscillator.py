"""Stochastic oscillator object.

In progress."""

import pandas as pd
from utils.assertions import items_of_sublist_in_list

from backtester.marketdatahelp import MarketDataService
from backtester.tradedatahelp import TradeDataService


class StochasticOscillator:
    """Stochastic osciallator object."""

    def __init__(self, data: pd.DataFrame, window_length: int = 14, **kwargs) -> None:
        self.data = data
        self.window_length = window_length

    def calculate(self) -> pd.DataFrame:
        """Calculate stochastic oscillator signal."""
        assert items_of_sublist_in_list(
            sublist=["High", "Low", "Close"], parent_list=self.data.columns
        )
        high_roll = self.data["High"].rolling(self.window_length).max()
        low_roll = self.data["Low"].rolling(self.window_length).min()

        # Fast stochastic indicator
        num = self.data["Close"] - low_roll
        denom = high_roll - low_roll
        stochastic_oscillator_df = pd.DataFrame()
        stochastic_oscillator_df["%K"] = (num / denom) * 100

        # Slow stochastic indicator
        stochastic_oscillator_df["%D"] = (
            stochastic_oscillator_df["%K"].rolling(3).mean()
        )

        return stochastic_oscillator_df


class StochasticOscillatorStrategy(StochasticOscillator):
    """Momentum strategy object."""

    def __init__(
        self, market_data: MarketDataService, trade_data: TradeDataService, **kwargs
    ) -> None:
        """Init."""
        strategy = kwargs.get("strategy", {})
        self.window_length = strategy.get("window_length", 14)
