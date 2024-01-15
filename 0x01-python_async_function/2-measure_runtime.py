#!/usr/bin/env python3
"""Measure the runtime"""


import asyncio
import time

wait = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n. Your function should return a float.
    """
    start = time.time()
    asyncio.run(wait(n, max_delay))
    end = time.time()
    return (end - start) / n
