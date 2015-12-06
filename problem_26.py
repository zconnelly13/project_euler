"""
Problem 26
==========

A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""


def recurring_cycle(n, d):
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0

cycles = [recurring_cycle(1, i) for i in range(2, 1001)]
maximum = cycles.index(max(cycles)) + 2
print(maximum)
