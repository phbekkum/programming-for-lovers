def sum_proper_divisors(n: int) -> int:
    """
    Return the sum of all proper (positive) divisors of n, i.e., divisors strictly less than n.
    """
    if n <= 1:
        return 0

    total = 1  # 1 is always a proper divisor for n > 1

    limit = int(n**0.5)
    for d in range(2, limit + 1):
        if n % d == 0:
            total += d
            other = n // d
            if other != d and other != n:
                total += other

    return total