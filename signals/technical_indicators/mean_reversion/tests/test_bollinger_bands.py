"""Test bollinger bands object functions."""

from static_data.test_static_data import ADJ_CLOSE_TRADE_DATA
import pandas as pd
from signals.technical_indicators.mean_reversion.bollinger_bands import BollingerBands
import numpy as np
from signals.technical_indicators.mean_reversion.tests.static_data import (
    BOLLINGER_BANDS_EXPECTED_OUTPUT,
)


class TestBollingerBands:
    """Test bollinger bands object."""

    def test_bollinger_bands(self):
        """Test bollinger bands."""
        trade_data = pd.Series(ADJ_CLOSE_TRADE_DATA)
        bbands = BollingerBands(
            data=trade_data, window_length=20, standard_deviations=2
        ).calculate()
        assert np.all(bbands[19:] == pd.Series(BOLLINGER_BANDS_EXPECTED_OUTPUT)[19:])
