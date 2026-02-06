import sys

def richness(sample: dict[str, int]) -> int:
    """
    Compute the richness of a frequency table.

    Args:
        sample: A frequency table mapping strings to occurrence counts.
    Returns:
        The richness of the sample.
    """
    count = 0
    for v in sample.values():
        if v > 0:
            count += 1
    return count