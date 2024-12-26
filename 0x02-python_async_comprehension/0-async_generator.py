#!/usr/bin/env python3
"""async generator"""
import asyncio
import random


async def async_generator():
    """return random async numbers"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
