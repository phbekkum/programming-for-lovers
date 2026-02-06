def power(a: int, b: int) -> int:
    result = 1
    for _ in range(b):
        result *= a
    return result


def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0:
        return False
    limit = int(x**0.5)
    for d in range(3, limit + 1, 2):
        if x % d == 0:
            return False
    return True


def list_mersenne_primes(n: int) -> list[int]:
    mersennes = []

    for p in range(1, n + 1):
        if is_prime(p):
            m = power(2, p) - 1
            if is_prime(m):
                mersennes.append(m)

    return mersennes