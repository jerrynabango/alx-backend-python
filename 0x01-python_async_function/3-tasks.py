#!/usr/bin/env python3
""" Tasks"""


import asyncio

wait = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returns a asyncio.Task"""
    return asyncio.create_task(wait(max_delay))
