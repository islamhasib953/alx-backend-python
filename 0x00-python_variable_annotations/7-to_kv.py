#!/usr/bin/env python3

""" function return a tuple of string and square of number as float """


def to_kv(k: str, v: int | float) -> tuple:
    """function take string and number float and
    return a tuple of string and square of number as float"""
    return (k, float(v * v))
