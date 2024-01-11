#!/usr/bin/env python3
from typing import Iterable, List, Sequence, Tuple
"""Let's duck type an iterable object"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
