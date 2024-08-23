#!/usr/bin/env python3

"""Task 1-async_comprehension"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async comprehensing"""
    return [num async for num in async_generator()]
