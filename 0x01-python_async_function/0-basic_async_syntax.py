#!/usr/bin/env python3
"""The basics of async"""
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument
        (max_delay, with a default value of 10) named wait_random
        that waits for a random delay between 0 and max_delay
        (included and float value) seconds and eventually returns it."""
    random_float = __import__('random').uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float

if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
