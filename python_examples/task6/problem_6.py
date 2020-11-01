"""
    Find the difference between the sum of the squares of the first one hundred natural
    numbers and the square of the sum.
"""


def get_result(n: int) -> int:
    sum_of_square_natural_numbers = sum([v * v for v in range(1, n+1)])
    square_of_sum_natural_numbers = pow(sum([v for v in range(1, n+1)]), 2)
    return square_of_sum_natural_numbers - sum_of_square_natural_numbers


print(f'Sum of n natural numbers and square of the sum is: {get_result(100)}')
