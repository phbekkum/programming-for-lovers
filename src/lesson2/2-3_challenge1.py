def fibonacci_array(n: int) -> list[int]:
    """
    Return an array of Fibonacci numbers from F₀ through Fₙ.
    """
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    fib = [1, 1] + [0] * (n - 1)

    for k in range(2, n + 1):
        fib[k] = fib[k - 1] + fib[k - 2]

    return fib