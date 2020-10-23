from utils.utils import is_prime

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def get_biggest_prime_factor(n: int) -> int:
    biggest_prime = -1
    prime_to_divide = 2
    while prime_to_divide <= n:
        if n % prime_to_divide == 0:
            n //= prime_to_divide
            biggest_prime = biggest_prime if biggest_prime > prime_to_divide else prime_to_divide
            prime_to_divide = 2
        else:
            while True:
                prime_to_divide += 1
                if is_prime(prime_to_divide):
                    break
    return biggest_prime


print(f'Biggest prime number is {get_biggest_prime_factor(600851475143)}')
