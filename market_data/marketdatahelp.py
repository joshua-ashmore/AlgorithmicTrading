"""Market data help objects."""

import pandas as pd


class MarketDataHelper:
    """Market data helper object.

    This needs to be re-written as market data helper is better defined."""

    def __init__(self, market_data, **kwargs) -> None:
        """Init."""
        assert type(market_data.market_data) == dict
        for _ac in market_data.market_data:
            data = market_data.market_data[_ac].data
            for _datum in data:
                # THIS IS WRONG
                market_data.market_data[_ac].data[_datum] = pd.Series(_datum)

    def if_dataframe(self, market_data: pd.DataFrame):
        if "Adj Close" in market_data.columns:
            self.data = market_data["Adj Close"]
        elif "Close" in market_data.columns:
            self.data = market_data["Close"]
        elif len(market_data.columns) == 1:
            self.data = pd.Series(market_data)
        else:
            raise ValueError
