#!/usr/bin/env python3
"""Module 1-concurrent_coroutines contains an async coroutine
that calls functions an sorts them by delay time
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that spawns wait_random and returns the list of all
    the delays (float values).
    The list of the delays are in ascending order without using sort()
    due to concurrency.

    Args:
        n (int): number of wait_random functions spawned and called
        max_delay (int): maximum seconds function can wait before return

    Returns:
        delays (list of floats): list of wait time (in seconds) delayed
    """
    coroutines = [asyncio.create_task(wait_random(max_delay))
                  for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(coroutines):
        delay = await task
        delays.append(delay)

    return delays
