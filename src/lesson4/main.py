import sys

def richness(sample: dict[str, int]) -> int:
    """
    Compute the richness (number of species with count > 0).
    """
    count = 0
    for v in sample.values():
        if v > 0:
            count += 1
    return count


def simpsons_index(sample: dict[str, int]) -> float:
    """
    Compute Simpson's index of a frequency table.
    """
    total = sum_of_values(sample)
    if total == 0:
        return 0.0

    index = 0.0
    for v in sample.values():
        if v > 0:
            p = v / total
            index += p * p
    return index


def sum_of_minima(sample1: dict[str, int], sample2: dict[str, int]) -> int:
    """
    Compute the sum of corresponding minimum values of two frequency tables.
    """
    total = 0
    for key in sample1:
        if key in sample2:
            total += min2(sample1[key], sample2[key])
    return total


def sum_of_maxima(sample1: dict[str, int], sample2: dict[str, int]) -> int:
    """
    Compute the sum of corresponding maximum values of two frequency tables.
    """
    total = 0
    all_keys = set(sample1.keys()) | set(sample2.keys())
    for key in all_keys:
        v1 = sample1.get(key, 0)
        v2 = sample2.get(key, 0)
        total += max2(v1, v2)
    return total


def bray_curtis_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:
    """
    Compute the Bray-Curtis distance between two frequency tables.
    """
    total1 = sum_of_values(sample1)
    total2 = sum_of_values(sample2)
    average = (total1 + total2) / 2.0
    shared = sum_of_minima(sample1, sample2)
    return 1 - (shared / average)


def jaccard_distance(sample1: dict[str, int], sample2: dict[str, int]) -> float:
    """
    Compute the Jaccard distance between two frequency tables.
    """
    sum_min = sum_of_minima(sample1, sample2)
    sum_max = sum_of_maxima(sample1, sample2)

    if sum_max == 0:
        return 0.0

    return 1 - (sum_min / sum_max)


# Provided helper functions
def min2(x: int, y: int) -> int:
    if x < y:
        return x
    return y

def max2(x: int, y: int) -> int:
    if x > y:
        return x
    return y