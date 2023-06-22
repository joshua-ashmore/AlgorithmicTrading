"""Test RSI object."""
import pandas as pd
from signals.technical_indicators.momentum.rsi import RSI
from static_data.test_static_data import ADJ_CLOSE_TRADE_DATA
from signals.technical_indicators.momentum.tests.static_data import (
    EMA_EXPECTED_OUTPUT,
    SMA_EXPECTED_OUTPUT,
)
import numpy as np


class TestRSIClass:
    """RSI object containing tests."""

    def test_rsi_ema(self):
        """Test RSI EWA."""
        trade_data = pd.Series(ADJ_CLOSE_TRADE_DATA)
        ema = RSI().calculate(
            data=trade_data, moving_average_type="EMA", window_length=14
        )
        assert np.all(ema == pd.Series(EMA_EXPECTED_OUTPUT))

    def test_rsi_sma(self):
        """Test RSI SMA."""
        trade_data = pd.Series(ADJ_CLOSE_TRADE_DATA)
        sma = RSI().calculate(
            data=trade_data, moving_average_type="SMA", window_length=14
        )
        assert np.all(sma[13:] == pd.Series(SMA_EXPECTED_OUTPUT)[13:])
