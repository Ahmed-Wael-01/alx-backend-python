#!/usr/bin/env python3
"""make tasks"""
import asyncio
from collections import Awaitable
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    return asyncio.create_task(wait_random(max_delay))
