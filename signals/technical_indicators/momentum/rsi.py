"""Relative strength index file."""

# from apis.data.trading_data import download_data
import pandas as pd
import numpy as np
import yfinance as yf
from typing import Union
from static_data.enums import MovingAverageTypes


def download_data(tickers: list, start_date: str, end_date: str, interval: str = "1d"):
    """Download trade data for given tickers."""
    return yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        interval=interval,
    )


class RSI:
    """Relative strength index object."""

    def calculate(
        self,
        data: Union[pd.DataFrame, pd.Series],
        moving_average_type: MovingAverageTypes,
        window_length: int = 14,
    ):
        """Calculate RSI."""
        data_diff = data.diff()
        data_diff.dropna(inplace=True)

        # Make the positive gains (up) and negative gains (down) Series
        pos, neg = data_diff.clip(lower=0), data_diff.clip(upper=0).abs()
        roll_up, roll_down = pd.DataFrame(), pd.DataFrame()
        if moving_average_type == "SMA":
            roll_up, roll_down = (
                pos.rolling(window=window_length).mean(),
                neg.rolling(window=window_length).mean(),
            )
        elif moving_average_type == "EMA":
            roll_up, roll_down = (
                pos.ewm(span=window_length).mean(),
                neg.ewm(span=window_length).mean(),
            )

        rs = roll_up / roll_down
        rsi = 100.0 - (100.0 / (1.0 + rs))

        rsi[:] = np.select([roll_down == 0, roll_up == 0, True], [100, 0, rsi])
        rsi.name = "rsi"

        valid_rsi = rsi[window_length - 1 :]  # noqa : E203
        assert ((0 <= valid_rsi) & (valid_rsi <= 100)).all()

        return rsi


trade_data = download_data(
    tickers=["AAPL"], start_date="2023-01-01", end_date="2023-03-01"
)
b = 1
