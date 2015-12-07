"""
Problem 39
==========

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""


from math import sqrt

upper_bound = 500

solutions = []


def perimeter(a, b):
    return a + b + sqrt(a**2 + b**2)

for a in range(0, upper_bound):
    for b in range(0, upper_bound):
        p = perimeter(a, b)
        if p == int(p):
            solutions.append(int(p))

print max(set(solutions), key=solutions.count)
