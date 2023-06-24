"""Backtester abstract code."""

import pandas as pd
import yfinance as yf

from backtester.marketdatahelp import MarketDataService
from backtester.tradedatahelp import TradeDataService

from signals.technical_indicators.trend.moving_average import MovingAverageStrategy
from signals.technical_indicators.mean_reversion.bollinger_bands import (
    BollingerBandsStrategy,
)

from static_data.test_static_data import AAPL_TRADE_DATA

example_payload = {
    "strategy": {
        "name": "MovingAverageStrategy",
        "moving_average_type": "SMA",
        "window_length": 14,
    },  # probably want to define all of these individually by object or make them modular -> definitely pydantic
    "dates": {"start_date": "2023-01-01", "end_date": "2023-03-01", "interval": "1d"},
    "eq_underlyings": ["AAPL"],
    "fx_underlyings": ["EURUSD"],
    "ir_underlyings": ["USD OIS", "EUR OIS"],
    "cm_underlyings": ["Jet Cargoes"],
}
DATE_STATIC_DATA = {
    "start_date": "2023-01-01",
    "end_date": "2023-03-01",
    "interval": "1d",
}


class BacktesterAPI:
    """Backtester api."""

    def __init__(self, **kwargs) -> None:
        """Init."""
        dates = kwargs.get("dates", DATE_STATIC_DATA)

        fx_underlyings = kwargs.get("fx_underlyings", [])
        eq_underlyings = kwargs.get("eq_underlyings", [])
        ir_underlyings = kwargs.get("ir_underlyings", [])
        cm_underlyings = kwargs.get("cm_underlyings", [])
        self.market_data = MarketDataService(
            fx_underlyings=fx_underlyings,
            eq_underlyings=eq_underlyings,
            ir_underlyings=ir_underlyings,
            cm_underlyings=cm_underlyings,
            dates=dates,
        )
        if kwargs.get("market_data", None) is not None:
            self.market_data = kwargs["market_data"]
            kwargs.pop("market_data")

        self.trade_data = TradeDataService(**kwargs)

        strategy = kwargs.get("strategy", {})
        strategy_name = strategy.get("name", "MovingAverageStrategy")
        f = self.api_to_backtest_strategy(strategy=strategy_name)
        self.strategy = f(
            market_data=self.market_data, trade_data=self.trade_data, **kwargs
        )
        self.signal = self.strategy.calculate()

    def api_to_backtest_strategy(self, strategy: str):
        """API which returns strategy object given string input."""
        return {
            "MovingAverageStrategy": MovingAverageStrategy,
            "BollingerBandsStrategy": BollingerBandsStrategy,
        }[strategy]


class Backtester:
    """Backtester object."""

    def __init__(
        self,
        start_date: str = "2023-01-01",
        end_date: str = "2023-03-01",
        interval: str = "1d",
        portfolio_value: float = 10_000,
        **kwargs,
    ):
        """Init."""
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval

        self.position_held = kwargs.get("position_held", False)
        self.current_position = kwargs.get("current_position", 0)

        self.position = (0, 0)
        self.initial_portfolio_value = portfolio_value
        self.returns = []
        self.data = pd.DataFrame()
        self.trading_parameters: list = []

    def run_backtester(self):
        """Logic to run backtester."""
        self.prepare_inputs()
        ticker_return_data = []
        for ticker_data in self.trading_parameters:
            self.portfolio_value = self.initial_portfolio_value
            self.trading_data(ticker_data)
            self.trading_logic()
            ticker_return_data.append(
                {
                    "tickers": ticker_data["index"],
                    "returns": self.returns,
                    "params": self.saved_params,
                }
            )
        return ticker_return_data

    def trading_logic(self):
        """Logic to trade."""
        self.returns = []
        self.saved_params = []
        for t in range(len(self.data)):
            self.t = t
            condition_to_continue = self.skip_functionality()
            if condition_to_continue:
                continue
            self.get_time_dependent_variables()
            if self.position_held is False:
                self.entry_trading_logic()
            elif self.position_held is True:
                self.exit_trading_logic()
            self.returns.append(
                {
                    "datetime": self.data.index[self.t],
                    "portfolio_value": self.portfolio_value,
                }
            )
            self.saved_params.append(self.params_to_save())

    def skip_functionality(self):
        """Functionality to skip tickers given conditions - abstracted."""
        return False

    def get_time_dependent_variables(self):
        """Get time dependent variables - abstracted."""
        pass

    def prepare_inputs(self):
        """Logic to prepare inputs - abstracted."""
        pass

    def params_to_save(self):
        """Params to save - abstracted."""
        pass

    def trading_data(self, ticker_data=None):
        """Logic to prepare trading data - abstracted."""
        pass

    def entry_trading_logic(self):
        """Entry trading logic - abstracted."""
        pass

    def exit_trading_logic(self):
        """Exit trading logic - abstracted."""
        pass

    def fetch_yahoo_finance_data(
        self,
        tickers: list[str],
        start_date: str,
        end_date: str,
        interval: str = "1d",
    ):
        """Fetch yahoo finance data."""
        data = yf.download(
            tickers=tickers,
            start=start_date,
            end=end_date,
            interval=interval,
        )
        return data


moving_average_strategy_payload = {
    "strategy": {
        "name": "MovingAverageStrategy",
        "moving_average_type": "EMA",
        "window_length": 5,
    },
    "market_data": AAPL_TRADE_DATA,
}
moving_average_results = BacktesterAPI(**moving_average_strategy_payload)

bollinger_band_strategy_payload = {
    "strategy": {
        "name": "BollingerBandsStrategy",
        "standard_deviations": 1,
        "window_length": 15,
    },
    "market_data": AAPL_TRADE_DATA,
}
bollinger_band_results = BacktesterAPI(**bollinger_band_strategy_payload)
