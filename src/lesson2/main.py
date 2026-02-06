def permutation(n: int, k: int) -> int:
    if k == 0:
        return 1
    result = 1
    for i in range(k):
        result *= (n - i)
    return result


def combination(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    perm = 1
    for i in range(k):
        perm *= (n - i)
    fact_k = 1
    for i in range(1, k + 1):
        fact_k *= i
    return perm // fact_k


def power(a: int, b: int) -> int:
    result = 1
    for _ in range(b):
        result *= a
    return result


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


def fibonacci_array(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    fib = [1, 1] + [0] * (n - 1)
    for k in range(2, n + 1):
        fib[k] = fib[k - 1] + fib[k - 2]
    return fib


def divides_all(a: list[int], d: int) -> bool:
    if d == 0:
        return False
    for x in a:
        if x % d != 0:
            return False
    return True


def max_integer_array(lst: list[int]) -> int:
    maximum = lst[0]
    for value in lst[1:]:
        if value > maximum:
            maximum = value
    return maximum


def max_integers(*numbers: int) -> int:
    if len(numbers) == 0:
        raise ValueError("At least one integer required")
    maximum = numbers[0]
    for value in numbers[1:]:
        if value > maximum:
            maximum = value
    return maximum


def sum_integers(*numbers: int) -> int:
    total = 0
    for value in numbers:
        total += value
    return total


def gcd_array(a: list[int]) -> int:
    abs_vals = [abs(x) for x in a]
    m = min(abs_vals)
    for d in range(m, 0, -1):
        ok = True
        for x in abs_vals:
            if x % d != 0:
                ok = False
                break
        if ok:
            return d
    return 0


def is_perfect(n: int) -> bool:
    if n <= 1:
        return False
    return sum_proper_divisors(n) == n


def next_perfect_number(n: int) -> int:
    candidate = n + 1
    while True:
        if is_perfect(candidate):
            return candidate
        candidate += 1


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


def next_twin_primes(n: int) -> tuple[int, int]:
    candidate = n + 1
    while True:
        if is_prime(candidate) and is_prime(candidate + 2):
            return (candidate, candidate + 2)
        candidate += 1