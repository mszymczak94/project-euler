"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def is_divided_by_prime(numbers_to_check: list, number: int) -> bool:
    for n in numbers_to_check:
        if number % n != 0:
            return False
    return True


def get_smallest_number_divided_by_all(n: int):
    number = n
    start = 1 if n < 6 else 6
    numbers_to_check = [i for i in range(start, n)]
    while True:
        if is_divided_by_prime(numbers_to_check, number):
            return number
        else:
            number += n


print(f'Smallest number divided by all values to n is: {get_smallest_number_divided_by_all(20)}')
