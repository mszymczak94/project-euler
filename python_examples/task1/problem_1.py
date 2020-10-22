"""
 * If we list all the natural numbers below 10 that are multiples of 3 or 5,
 * we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_sum_of_numbers_divided_by_3_or_5(n: int) -> int:
    numbers = [k for k in range(n) if k % 3 == 0 or k % 5 == 0]
    return sum(numbers)


print(f'Sum of all numbers is {get_sum_of_numbers_divided_by_3_or_5(1000)}')
