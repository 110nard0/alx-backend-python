#!/usr/bin/env python3
"""Module 4-tasks contains a function that spawns async processes
and returns a list of their delays
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that spawns the task_wait_random function and
    returns the list of all the delays (float values)
    The list of the delays are in ascending order without using
    sort() due to concurrency

    Args:
        n (int): number of task_wait_random functions spawned and called
        max_delay (int): maximum seconds function can wait before returning

    Returns:
        delays (list of floats): list of wait time (in seconds) delayed
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
