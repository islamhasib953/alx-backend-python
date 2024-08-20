#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier takes a float multiplier as argument
    and returns a function multiplies a float by multiplier."""

    def multiply(n: float) -> float:
        """Function that takes a float and
        returns its product with multiplier"""
        return n * multiplier

    return multiply
