from cachetools import cached, LRUCache, TTLCache
import numpy as np
import pandas as pd
from typing import Union


def percent(num, denom):
    return (100 * (num / float(denom))) if denom else 0


def percent_str(num, denom):
    return str(percent) + "%"


@cached({})
def discretise(
    val,
    increment: Union[int, float] = 0.1,
    lower: Union[int, float] = 0.0,
    upper: Union[int, float] = 1.0,
    enforce_range: bool = False,
):
    @cached({})
    def calc_increments(increment, lower, upper):
        assert (
            lower <= increment <= upper
        ), f"Required: {lower:.2f} < {increment:.2f} <= {upper:.2f}"
        # e.g. for lower=0, upper=1, increment_size=0.05, nincrements=21
        nincrements = int((upper - lower) / increment) + 1
        # e.g. for lower=0, upper=1, increment_size=0.05, increments = [0., 0.05, 0.1, ..., 0.95, 1. ]
        increments = np.linspace(lower, upper, nincrements)
        return increments

    if pd.isnull(val):
        return upper
    if enforce_range:
        assert (
            lower <= val <= upper
        ), f"Required: {lower:.2f} < {val:.2f} <= {upper:.2f}"
    increments = calc_increments(increment, lower, upper)
    if val < lower:
        return increments[0]
    if val > upper:
        return increments[-1]
    idx = np.digitize(val, increments)
    # e.g.
    #   0.00 -> 0.0
    #   0.01 -> 0.0
    #   0.06 -> 0.05
    #   0.99 -> 0.95
    #   1.00 -> 1.0
    discretised = increments[idx - 1]
    return discretised
