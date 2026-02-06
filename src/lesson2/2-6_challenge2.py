def permutation(n: int, k: int) -> int:
    if k == 0:
        return 1
    result = 1
    for i in range(k):
        result *= (n - i)
    return result