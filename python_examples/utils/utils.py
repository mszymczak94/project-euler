from math import sqrt


def get_prime_numbers(n: int) -> list:
    primes = [i for i in range(0, n + 1)]
    primes[1] = 0
    stop_index = int(sqrt(n)) + 1
    for i in range(2, stop_index):
        j = i + i
        while j <= n:
            primes[j] = 0
            j += i
    return list(filter(lambda i: i != 0, primes))


def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is_palindrome(n: str) -> bool:
    length = len(n)
    last_char = len(n) - 1
    for char in n:
        if char != n[last_char]:
            return False
        last_char -= 1
        if last_char < length//2:
            break
    return True
