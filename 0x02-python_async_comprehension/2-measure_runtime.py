"""Module 2-measure_runtime"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that executes async_comprehension task 4 times in parallel,
    measures the total runtime and returns that value

    Return:
        total_runtime (float): total (max) time each coroutine spends in thread
    """
    tasks = []

    for _ in range(4):
        task = asyncio.create_task(async_comprehension())
        tasks.append(task)

    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
