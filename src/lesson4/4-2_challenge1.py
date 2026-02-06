import sys

def sum_of_minima(sample1: dict[str, int], sample2: dict[str, int]) -> int:

    total = 0

    for key in sample1:
        if key in sample2:
            total += min2(sample1[key], sample2[key])

    return total


def min2(x: int, y: int) -> int:
    if x < y:
        return x
    return y