"""Test on balance volume."""

from signals.technical_indicators.volume.on_balance_volume import OnBalanceVolume
from static_data.test_static_data import AAPL_TRADE_DATA
import pandas as pd
from signals.technical_indicators.volume.tests.static_data import (
    ON_BALANCE_VOLUME_EXPECTED_OUTPUT,
)
import numpy as np


class TestOnBalanceVolume:
    """Test on balance volume object."""

    def test_on_balance_volume(self):
        """Test on balance volume."""
        trade_data = pd.DataFrame(AAPL_TRADE_DATA)
        obv = OnBalanceVolume().calculate(data=trade_data)
        assert np.all(obv == pd.Series(ON_BALANCE_VOLUME_EXPECTED_OUTPUT))
