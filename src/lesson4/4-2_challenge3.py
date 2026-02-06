import sys

def sum_of_maxima(sample1: dict[str, int], sample2: dict[str, int]) -> int:

    total = 0

    all_keys = set(sample1.keys()) | set(sample2.keys())

    for key in all_keys:
        v1 = sample1.get(key, 0)
        v2 = sample2.get(key, 0)
        total += max2(v1, v2)

    return total


def max2(x: int, y: int) -> int:
    if x > y:
        return x
    return y