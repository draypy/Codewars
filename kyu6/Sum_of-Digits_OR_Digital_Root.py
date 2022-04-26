"""
https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
"""
from functools import reduce


def digital_root(n):
    if n < 10:
        return n
    return digital_root(reduce(lambda x, y: int(x) + int(y), str(n)))
