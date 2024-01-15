#!/usr/bin/env python3
"""Tasks"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of asyncio.Task"""
    resolves = await asyncio.gather(
        *(task_wait_random(max_delay) for task in range(n)))
    return sorted(resolves)
