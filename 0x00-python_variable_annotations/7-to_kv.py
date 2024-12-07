#!/usr/bin/env python3
"""making a weird tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuble"""
    return (k, float(v * v))
