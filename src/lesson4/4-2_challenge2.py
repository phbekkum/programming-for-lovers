import sys

def bray_curtis_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:

    total1 = sum_of_values(sample1)
    total2 = sum_of_values(sample2)

    average = (total1 + total2) / 2.0
    shared = sum_of_minima(sample1, sample2)

    return 1 - (shared / average)


def min2(x: int, y: int) -> int:
    if x < y:
        return x
    return y