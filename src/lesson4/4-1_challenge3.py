import sys

def simpsons_index(sample: dict[str, int]) -> float:

    total = sum_of_values(sample)
    if total == 0:
        return 0.0

    index = 0.0
    for v in sample.values():
        if v > 0:
            p = v / total
            index += p * p

    return index