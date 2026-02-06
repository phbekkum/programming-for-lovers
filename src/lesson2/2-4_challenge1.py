def sum_proper_divisors(n: int) -> int:
    if n <= 1:
        return 0

    total = 1
    limit = int(n**0.5)

    for d in range(2, limit + 1):
        if n % d == 0:
            total += d
            other = n // d
            if other != d and other != n:
                total += other

    return total


def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    return sum_proper_divisors(n) == n