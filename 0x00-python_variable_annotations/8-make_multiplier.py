#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies float by multiplier"""
    def types(f: float) -> float:
        """Return product of multiplier and float"""
        return multiplier * f
    return types
