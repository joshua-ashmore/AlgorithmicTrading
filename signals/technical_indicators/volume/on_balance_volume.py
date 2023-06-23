"""On balance volume indicator."""

import pandas as pd
from utils.assertions import items_of_sublist_in_list
import numpy as np


class OnBalanceVolume:
    """On balance volume object."""

    def calculate(self, data: pd.DataFrame) -> pd.Series:
        """Calculate on balance volume."""
        assert items_of_sublist_in_list(
            sublist=["Close", "Volume"], parent_list=data.columns
        )
        return (np.sign(data["Close"].diff()) * data["Volume"]).fillna(0).cumsum()


def subfinder(mylist, pattern):
    return list(filter(lambda x: x in pattern, mylist))
