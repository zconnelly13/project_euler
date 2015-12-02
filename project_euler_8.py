"""
Problem 8
=========

The four adjacent digits in the 1000-digit number that have the greatest
product are 9 x 9 x 8 x 9 = 5832.

(see data.problem_8.series)

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""


from data.problem_8 import series

product = max(
    [reduce(lambda x, y: int(x) * int(y),
     series[start:start+13])
     for start in xrange(0, len(series))
     if start < len(series) - 13])

print(product)
