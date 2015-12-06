"""
Problem 28
==========

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20 7 8 9 10
19 6 1 2 11
18 5 4 3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?
"""

"""
Notes:

    Given a (n x n) grid formed this way, the top right number is
    n^2, then going counterclockwise around
    (n^2) - n + 1
    (n^2) - 2n + 2
    (n^2) - 3n + 3

    adding these we get 4n^2 - 6n + 6
    so sum this in steps of two starting at 3 and going to 1001
    (we tack on 1 at the end to account for the 1 in the middle of
    the spiral)
"""


from tools import quadratic


s = sum([quadratic(4, -6, 6)(n) for n in range(3, 1002, 2)]) + 1
print(s)
