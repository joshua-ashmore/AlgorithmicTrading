"""Moving average technical indicator object."""

from static_data.enums import MovingAverageTypes

from backtester.marketdatahelp import MarketDataService
from backtester.tradedatahelp import TradeDataService

from market_data.marketdatahelp import MarketDataHelper


class MovingAverage:
    """Moving average object."""

    def __init__(
        self,
        data,
        moving_average_type: MovingAverageTypes,
        window_length: int = 14,
        **kwargs,
    ) -> None:
        """Init.

        Args:
            data (_type_): market data
            moving_average_type (MovingAverageTypes): type of moving average
            window_length (int, optional): length of lookback window. Defaults to 14.
        """
        self.data = data
        self.moving_average_type = moving_average_type
        self.window_length = window_length

    def calculate(self):
        """Calculate moving average."""
        if self.moving_average_type == "SMA":
            return self.data.rolling(window=self.window_length).mean()
        elif self.moving_average_type == "EMA":
            return self.data.ewm(span=self.window_length).mean()


class MovingAverageStrategy(MarketDataHelper, MovingAverage):
    """Momentum strategy object."""

    def __init__(
        self, market_data: MarketDataService, trade_data: TradeDataService, **kwargs
    ) -> None:
        """Init."""
        super().__init__(market_data, **kwargs)
        strategy = kwargs.get("strategy", {})
        self.moving_average_type = strategy.get("moving_average_type", "SMA")
        self.window_length = strategy.get("window_length", 14)
