# Insert your sum_first_n_integers() function here.
def sum_first_n_integers(n: int) -> int:
    """
    Takes as input an integer n and returns the sum of the first n positive integers.
    Parameters:
    - n (int): an integer
    Returns:
    int: sum of the first n positive integers
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total