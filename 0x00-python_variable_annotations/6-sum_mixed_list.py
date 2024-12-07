#!/usr/bin/env python3
"""sums a list of mixed num types"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """returns sum of mixed list"""
    return float(sum(mxd_lst))
