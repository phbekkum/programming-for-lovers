def combination(n: int, k: int) -> int:
    """
    Compute the combination statistic C(n, k) = n! / ((n - k)! * k!).
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # Compute P(n, k) = n * (n-1) * ... * (n-k+1)
    perm = 1
    for i in range(k):
        perm *= (n - i)

    # Compute k! 
    fact_k = 1
    for i in range(1, k + 1):
        fact_k *= i

    return perm // fact_k