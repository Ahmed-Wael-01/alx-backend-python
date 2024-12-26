#!/usr/bin/env python3
"""multiple routines"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return sorted list of random float values"""
    arr = []
    for task in asyncio.as_completed(
            [task_wait_random(max_delay) for i in range(n)]):
        arr.append(await task)
    return arr
