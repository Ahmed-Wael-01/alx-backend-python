#!/usr/bin/env python3
"""multiple routines"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return sorted list of random float values"""
    arr = []
    for task in asyncio.as_completed(
            [wait_random(max_delay) for i in range(n)]):
        arr.append(await task)
    return arr
