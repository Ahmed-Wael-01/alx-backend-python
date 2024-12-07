#!/usr/bin/env python3
"""duck typng annotation"""
from typing import Sequence, List, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return the correct type"""
    return [(i, len(i)) for i in lst]
