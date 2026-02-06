def gcd_array(a: list[int]) -> int:
    """
    Return the greatest common divisor (GCD) of all integers in the list.
    """
    # Work with absolute values, since gcd is always non‑negative
    abs_vals = [abs(x) for x in a]

    # The gcd cannot be larger than the smallest absolute value
    m = min(abs_vals)

    # Try divisors from m down to 1
    for d in range(m, 0, -1):
        ok = True
        for x in abs_vals:
            if x % d != 0:
                ok = False
                break
        if ok:
            return d

    return 0