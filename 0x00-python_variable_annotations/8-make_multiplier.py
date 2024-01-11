#!/usr/bin/env python3
"""Complex types - functions"""


def make_multiplier(multiplier: float) -> float:
    """Return function that multiplies float by multiplier"""
    return lambda x: x * multiplier
