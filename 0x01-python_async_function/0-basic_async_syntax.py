#!/usr/bin/env python3

""" waits for a random delay """
import random, asyncio


async def wait_random(max_delay: int = 10):
    """waits for a random delay between 0 and max_delay seconds and returns it."""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
