"""
Problem 11
==========

In the 20x20 grid below, four numbers along a diagonal line have been marked in
red.

(see data/problem_11.py)

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20x20 grid?
"""


from data.problem_11 import grid
from itertools import izip_longest
from itertools import product
from operator import add


# start with directions in the first quadrant

directions = zip(*[[(x, 0), (0, x), (x, x), (-x, x)] for x in range(0, 4)])
coordinates = [coordinate for coordinate in
               product(range(len(grid)), range(len(grid[0])))]


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def get(c):
    x, y = c
    try:
        value = grid[x][y]
    except IndexError:
        value = 0
    return value


def products(coordinate):
    coordinate_sets = grouper(
        [tuple(map(add, coordinate, direction_coordinate))
         for direction in directions
         for direction_coordinate in direction], 4)
    return [
        reduce(lambda total, coordinate: (total * get(coordinate)),
               coordinate_set, 1)
        for coordinate_set in coordinate_sets]

maximum = max([max(products(coordinate)) for coordinate in coordinates])
print(maximum)
