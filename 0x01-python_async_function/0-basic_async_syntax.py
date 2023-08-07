#!/usr/bin/env python3
"""Module 0-basic_async_syntax.py contains an asynchronous coroutine
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async coroutine takes in an int parameter, waits for a random
    delay - between 0 and argument seconds - and eventually returns it

    Argument:
        max_delay (int): max delay that async functipn can suspend operations

    Return:
        delay (float): delay that async function waits before returning
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
