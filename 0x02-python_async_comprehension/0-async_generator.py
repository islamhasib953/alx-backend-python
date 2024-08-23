#!/usr/bin/env python3

""" Task 0-async_generator """
import asyncio, random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine called async_generator that takes no arguments."""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
