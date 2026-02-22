def euclid_gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def relatively_prime(a: int, b: int) -> bool:
    return euclid_gcd(abs(a), abs(b)) == 1