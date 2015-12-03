"""
Problem 18
==========

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

(see data.problem_18.triangle)


NOTE: As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67, is the same challenge with
a triangle containing one-hundred rows; it cannot be solved by brute
force, and requires a clever method! ;o)
"""

from data.problem_18 import triangle


def scrunch(bigger_row, smaller_row):
    """Climb the tree from the bottom taking the greatest sum as you go

    """
    def get(l, index):
        """'Safe' get method for lists

        """
        try:
            value = l[index]
        except IndexError:
            value = 0
        return value
    # return the greatest sum out of the two touching numbers in the tree
    return [max([value+get(bigger_row, i), value+get(bigger_row, i+1)])
            for i, value in enumerate(smaller_row)]

scrunched = reduce(
    scrunch,
    triangle[::-1])[0]

print(scrunched)
