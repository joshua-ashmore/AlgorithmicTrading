"""Test stochastic oscillator."""

from signals.technical_indicators.relative_strength.stochastic_oscillator import (
    StochasticOscillator,
)
from static_data.test_static_data import AAPL_TRADE_DATA
import pandas as pd
from signals.technical_indicators.relative_strength.tests.static_data import (
    STOCHASTIC_OSCILLATOR_EXPECTED_OUTPUT,
)
import numpy as np


class TestStochasticOscillator:
    """Test stochastic oscillator object."""

    def test_stochastic_oscillator(self):
        """Test stochastic oscillator."""
        trade_data = pd.DataFrame(AAPL_TRADE_DATA)
        stochastic_oscillator = StochasticOscillator().calculate(
            data=trade_data, window_length=14
        )
        assert np.all(
            stochastic_oscillator["%K"][13:]
            == pd.DataFrame(STOCHASTIC_OSCILLATOR_EXPECTED_OUTPUT)["%K"][13:]
        )
        assert np.all(
            stochastic_oscillator["%D"][15:]
            == pd.DataFrame(STOCHASTIC_OSCILLATOR_EXPECTED_OUTPUT)["%D"][15:]
        )
