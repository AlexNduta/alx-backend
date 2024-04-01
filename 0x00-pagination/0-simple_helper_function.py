#!/usr/bin/env python3
""" module level doc"""
from typing import Tuple


def index_range(page: int, size:int)->Tuple[int, int]:
    """ returns the first and last index"""
    # index_range(1,7) = index 0 and index 7
    # index_rnage(3, 15) = index 30 index 45
    end_index = page * size
    start_index = end_index - size
    return (start_index, end_index)
