#!/usr/bin/env python3

""" function return a tuple of string and square of number as float """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function take string and number float and
    return a tuple of string and square of number as float"""
    return (k, v * v)
