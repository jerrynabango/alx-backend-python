#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather
    """
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for compre in range(4)))
    end: float = time.perf_counter()
    return (end - start)
