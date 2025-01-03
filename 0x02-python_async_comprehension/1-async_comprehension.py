#!/usr/bin/env python3
"""async generator comp"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension"""
    arr = [i async for i in async_generator()]
    return arr
