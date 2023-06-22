"""Enums for all classes."""

from pydantic import BaseModel


class MovingAverageModel(BaseModel):
    """Moving average pydantic base model."""

    name: str


class MovingAverageTypes(MovingAverageModel):
    sma = MovingAverageModel(name="SMA")
    ema = MovingAverageModel(name="EMA")
