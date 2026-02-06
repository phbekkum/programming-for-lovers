def permutation(n: int, k: int) -> int:
    """
    Compute the permutation statistic P(n, k) = n · (n-1) · ... · (n-k+1).
    """
    if k == 0:
        return 1

    result = 1
    for i in range(k):
        result *= (n - i)

    return result