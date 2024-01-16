#!/usr/bin/env python3
"""Async Comprehensions"""

from typing import Generator
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    The coroutine will collect 10 random numbers using an
    async comprehensing over async_generator,
    then return the 10 random numbers.
    """
    return [compre async for compre in async_generator()]

if __name__ == "__main__":
    asyncio.run(async_comprehension())
