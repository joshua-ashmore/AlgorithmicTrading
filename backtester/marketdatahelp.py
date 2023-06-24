"""Market data help."""

import yfinance as yf
from datetime import datetime


def download_data(tickers: list, start_date: str, end_date: str, interval: str = "1d"):
    """Download trade data for given tickers."""
    return yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        interval=interval,
    )


def future_code_helper(date=None) -> str:
    """Returns correct future code given current time/starting time in month."""
    MONTH_CODE_HELPER = {
        1: "F",
        2: "G",
        3: "H",
        4: "J",
        5: "K",
        6: "M",
        7: "N",
        8: "Q",
        9: "U",
        10: "V",
        11: "X",
        12: "Z",
    }
    current_date = date or datetime.now().date()
    if type(current_date) == str:
        current_date = datetime.strptime(current_date, "%Y-%m-%d")
    assert type(current_date) == datetime
    year = current_date.year
    month = current_date.month
    day = current_date.day
    if month % 3 == 0 and day >= 20:
        month += 1
    while month % 3 != 0:
        month += 1
    return MONTH_CODE_HELPER[month] + str(year)[:2]


CURRENCY_IR_MAP = {
    "USD": "SR3",
    "GBP": "SON",
    # looks like there's no EONIA on yfinance
}


class DateHandler:
    """Date handler object."""

    def __init__(self, dates: dict) -> None:
        self.start_date = dates.get("start_date", "2023-01-01")
        self.end_date = dates.get("end_date", "2023-03-01")
        self.interval = dates.get("interval", "1d")


class FXDataHandler(DateHandler):
    """FX data handler object."""

    def __init__(self, fx_underlyings, dates, **kwargs) -> None:
        """Initialise and fetch data."""
        super().__init__(dates)
        self.data = []
        for underlying in fx_underlyings:
            if underlying[:2] != "=X":
                underlying = underlying + "=X"
            self.data.append(
                {
                    underlying: download_data(
                        tickers=underlying,
                        start_date=self.start_date,
                        end_date=self.end_date,
                        interval=self.interval,
                    ).to_dict()
                }
            )


class EQDataHandler(DateHandler):
    """EQ data handler object."""

    def __init__(self, eq_underlyings, dates: dict) -> None:
        """Initialise and fetch data.

        Should this be able to access both spot prices and option prices?
        """
        super().__init__(dates)
        self.data = []
        for underlying in eq_underlyings:
            self.data.append(
                {
                    underlying: download_data(
                        tickers=underlying,
                        start_date=self.start_date,
                        end_date=self.end_date,
                        interval=self.interval,
                    ).to_dict()
                }
            )


class IRDataHandler(DateHandler):
    """IR data handler object."""

    def __init__(self, ir_underlyings, dates, **kwargs) -> None:
        """Initialise and fetch data.

        Can't currently return historical OIS data given yfinance limitations."""
        super().__init__(dates)
        self.data = []
        fut_code_str = future_code_helper(date=self.start_date)
        for underlying in ir_underlyings:
            assert underlying in CURRENCY_IR_MAP.keys()
            ir_ticker = CURRENCY_IR_MAP[underlying] + fut_code_str + ".CME"
            self.data.append(
                {
                    underlying: download_data(
                        tickers=[ir_ticker],
                        start_date=self.start_date,
                        end_date=self.end_date,
                        interval=self.interval,
                    ).to_dict()
                }
            )


class CMDataHandler(DateHandler):
    """CM data handler object."""

    def __init__(self, cm_underlyings, dates, **kwargs) -> None:
        """Initialise and fetch data."""
        super().__init__(dates)
        self.data = []
        for underlying in cm_underlyings:
            if underlying[:2] != "=F":
                underlying = underlying + "=F"
            self.data.append(
                {
                    underlying: download_data(
                        tickers=underlying,
                        start_date=self.start_date,
                        end_date=self.end_date,
                        interval=self.interval,
                    ).to_dict()
                }
            )


class MarketDataService:
    """Market data object.

    Should be able to request/return market data given underlyings/asset classes."""

    def __init__(
        self,
        fx_underlyings: list = [],
        eq_underlyings: list = [],
        ir_underlyings: list = [],
        cm_underlyings: list = [],
        dates: dict = {},
        **kwargs,
    ) -> None:
        """Init and prepare market data."""
        self.fx_data = FXDataHandler(
            fx_underlyings=fx_underlyings, dates=dates, **kwargs
        )
        self.eq_data = EQDataHandler(
            eq_underlyings=eq_underlyings, dates=dates, **kwargs
        )
        self.ir_data = IRDataHandler(
            ir_underlyings=ir_underlyings, dates=dates, **kwargs
        )
        self.cm_data = CMDataHandler(
            cm_underlyings=cm_underlyings, dates=dates, **kwargs
        )

        self.market_data = {
            "fx_data": self.fx_data,
            "eq_data": self.eq_data,
            "ir_data": self.ir_data,
            "cm_data": self.cm_data,
        }
