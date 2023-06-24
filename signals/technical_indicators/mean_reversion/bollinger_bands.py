"""Bollinger bands objects."""

import pandas as pd

from backtester.marketdatahelp import MarketDataService
from backtester.tradedatahelp import TradeDataService

from market_data.marketdatahelp import MarketDataHelper


class BollingerBands:
    """Bollinger bands object."""

    def __init__(
        self, data, standard_deviations: int = 2, window_length: int = 20, **kwargs
    ) -> None:
        """Init."""
        self.data = data
        self.standard_deviations = standard_deviations
        self.window_length = window_length

    def calculate(self) -> pd.Series:
        """Calculate bollinger bands signal."""
        rolling = self.data.rolling(self.window_length)
        if self.standard_deviations == 0:
            bband = rolling.mean()
        else:
            bband = rolling.mean() + rolling.std(ddof=0) * self.standard_deviations
        return bband


class BollingerBandsStrategy(MarketDataHelper, BollingerBands):
    """Bollinger bands object."""

    def __init__(
        self, market_data: MarketDataService, trade_data: TradeDataService, **kwargs
    ) -> None:
        """Init."""
        super().__init__(market_data, **kwargs)
        strategy = kwargs.get("strategy", {})
        self.standard_deviations = strategy.get("standard_deviations", 2)
        self.window_length = strategy.get("window_length", 20)
