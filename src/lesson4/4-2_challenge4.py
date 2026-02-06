import sys

def jaccard_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:

    sum_min = sum_of_minima(sample1, sample2)
    sum_max = sum_of_maxima(sample1, sample2)

    if sum_max == 0:
        return 0.0

    return 1 - (sum_min / sum_max)


def min2(x: int, y: int) -> int:
    if x < y:
        return x
    return y

def max2(x: int, y: int) -> int:
    if x > y:
        return x
    return y