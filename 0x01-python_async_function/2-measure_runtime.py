#!/usr/bin/env python3
"""Module 2-measure_runtime contains a function that times an async coroutine
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Takes two int parameters and measures total execution time for
    each async coroutine and returns the total time / number of coroutine

    Args:
        n (int): number of wait_n tasks spawned
        max_delay (int): maximum delay that a wait_n function lasts

    Returns:
        delayed (float): elapsed time / number of spawned coroutines
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
