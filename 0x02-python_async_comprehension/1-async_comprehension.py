#!/usr/bin/env python3
"""Async Comprehensions"""


import asyncio
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """coroutine called async_comprehension that takes no arguments"""
    return [a async for a in async_generator()]
