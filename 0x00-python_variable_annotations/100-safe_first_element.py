#!/usr/bin/env python3
"""first element of a sequence"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return first element"""
    if lst:
        return lst[0]
    else:
        return None
