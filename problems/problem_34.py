"""
Problem 34
==========

145 is a curious number, as 1! + 4! + 5! = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits
"""

from math import factorial

def sum_of_factorial_of_digits(n):
    return sum([factorial(int(d)) for d in str(n)])

curious_numbers = [
    n
    for n in range(3, 100000)
    if n == sum_of_factorial_of_digits(n)]

total = sum(curious_numbers)
print(total)
