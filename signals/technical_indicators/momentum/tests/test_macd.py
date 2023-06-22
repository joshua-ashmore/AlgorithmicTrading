"""Test MACD function."""

from static_data.test_static_data import ADJ_CLOSE_TRADE_DATA
from signals.technical_indicators.momentum.macd import MACD
from signals.technical_indicators.momentum.tests.static_data import MACD_EXPECTED_OUTPUT
import pandas as pd
import numpy as np


class TestMACD:
    """Test MACD object."""

    def test_macd(self):
        """Test macd."""
        trade_data = pd.Series(ADJ_CLOSE_TRADE_DATA)
        macd_signal = MACD().calculate(
            data=trade_data,
            short_window_length=12,
            long_window_length=26,
            smooth_window_length=9,
        )
        assert np.all(macd_signal == pd.Series(MACD_EXPECTED_OUTPUT))
