#!/usr/bin/env python3
"""Module 1-async_comprehension
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine collects 10 random numbers using an async
    comprehension over an async function then returns them

    Return:
        [float]: list of random float values
    """
    return [num async for num in async_generator()]
