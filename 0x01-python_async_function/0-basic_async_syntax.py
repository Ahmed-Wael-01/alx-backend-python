#!/usr/bin/env python3
"""async random module"""
import random
import asyncio


async def wait_random(max_delay=10):
    """return random float"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
