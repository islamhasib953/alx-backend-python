#!/usr/bin/env python3
from typing import List

""" sum List of float numbers """


def sum_list(input_list: List[float]) -> float:
    """function takes float number and return sum of it"""
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
