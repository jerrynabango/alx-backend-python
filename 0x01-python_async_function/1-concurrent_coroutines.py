#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay
    """
    queue, array = [], []
    for _ in range(n):
        queue.append(wait_random(max_delay))
    for asyn in asyncio.as_completed(queue):
        result = await asyn
        array.append(result)
    return array
