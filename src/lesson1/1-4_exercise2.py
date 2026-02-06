# Insert your sum_even() function here.
def sum_even(k: int) -> int:
    """
    Takes as input an integer k and returns the sum of all even positive integers
    up to and (possibly) including k.
    """
    total = 0
    for i in range(2, k + 1, 2):
        total += i
    return total