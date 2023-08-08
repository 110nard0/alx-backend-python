#!/usr/bin/env python3
"""Module 3-tasks contains a function that spawns and returns an async process
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an int argument and return an asyncio task that waits
    a specified amount of time and then returns the coroutine

    Argument:
        max_delay (int): maximum delay wait_random function can wait

    Return:
        class <_asyncio.Task> instance object
    """
    coroutine = wait_random(max_delay)
    return asyncio.ensure_future(coroutine)
