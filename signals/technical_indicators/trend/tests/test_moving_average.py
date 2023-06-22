"""Test moving average calculation."""

import pandas as pd
from signals.technical_indicators.trend.moving_average import MovingAverage
from static_data.test_static_data import ADJ_CLOSE_TRADE_DATA
from signals.technical_indicators.trend.tests.static_data import (
    SMA_EXPECTED_OUTPUT,
    EMA_EXPECTED_OUTPUT,
)
import numpy as np


class TestMovingAverage:
    """Test moving average calculations."""

    def test_simple_moving_average(self):
        """Test simple moving average."""
        trade_data = pd.Series(ADJ_CLOSE_TRADE_DATA)
        sma = MovingAverage().calculate(
            data=trade_data, moving_average_type="SMA", window_length=14
        )
        assert np.all(sma[13:] == pd.Series(SMA_EXPECTED_OUTPUT)[13:])

    def test_exponentially_weighted_moving_average(self):
        """Test exponentially weighted moving average."""
        trade_data = pd.Series(ADJ_CLOSE_TRADE_DATA)
        ema = MovingAverage().calculate(
            data=trade_data, moving_average_type="EMA", window_length=14
        )
        assert np.all(ema == pd.Series(EMA_EXPECTED_OUTPUT))
