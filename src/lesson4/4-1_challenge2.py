import sys

def sum_of_values(sample: dict[str, int]) -> int:
   
    total = 0
    for value in sample.values():
        total += value
    return total