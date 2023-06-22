"""YFinance API."""

import yfinance as yf


def download_data(tickers: list, start_date: str, end_date: str, interval: str = "1d"):
    """Download trade data for given tickers."""
    return yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        interval=interval,
    )
