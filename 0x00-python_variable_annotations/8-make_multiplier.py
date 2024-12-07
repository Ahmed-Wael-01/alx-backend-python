#!/usr/bin/env python3
"""making a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a dynamic function"""
    def f(n: float) -> float:
        """hi there"""
        return n * multiplier

    return f
