"""Simulates use of the backtester API."""

from backtester.backtesterhelp import BacktesterAPI

payload = {
    "strategy": {
        "name": "MovingAverageStrategy",
        "moving_average_type": "SMA",
        "window_length": 14,
    },
    "dates": {"start_date": "2023-01-01", "end_date": "2023-03-01", "interval": "1d"},
    "eq_underlyings": ["AAPL"],
    "ir_underlyings": ["USD", "GBP"],
    "cm_underlyings": ["ZC"],
    "fx_underlyings": ["GBPUSD"],
}
ma_strat = BacktesterAPI(**payload)
b = 1
