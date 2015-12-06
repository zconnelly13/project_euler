"""
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.

(see data/problem_13)
"""

from data.problem_13 import numbers

print(str(sum(numbers))[0:10])
