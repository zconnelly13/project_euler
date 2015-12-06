"""
Problem 9
=========

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


from itertools import product

candidates = xrange(1, 1000)

for a, b, c in product(candidates, candidates, candidates):
    if a+b+c == 1000 and a**2 + b**2 == c**2:
        print(a*b*c)
        break
