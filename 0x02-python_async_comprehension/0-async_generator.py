#!/usr/bin/env python3
"""Module 0-async_generator"""

import asyncio
import random


async def async_generator() -> float:
    """This coroutine takes no arguments, loops 10 times, each time
    asynchronously waits 1 sec, then yields a rand number > 0 && < 10

    Return:
        Yields a random float value
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
