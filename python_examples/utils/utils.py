from math import sqrt


def get_prime_numbers(n: int) -> list:
    primes = [True for i in range(0, n + 1)]
    primes[1] = 0
    stop_index = int(sqrt(n)) + 1
    for i in range(2, stop_index):
        j = i + i
        while j < n:
            print(j)
            primes[j] = 0
            j += i
    return list(filter(lambda i: i != 0, primes))


def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i: int = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
