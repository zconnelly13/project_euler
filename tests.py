"""
Test that all of the solutions still work and are correct
This is necessary because some solutions share code in `tools`
"""

import unittest
import sys
from cStringIO import StringIO
from nose_parameterized import parameterized

SOLUTIONS = {
    1: 233168,
    2: 4613732,
    3: 6857,
    4: 906609,
    5: 232792560,
    6: 25164150,
    7: 104743,
    8: 23514624000,
    9: 31875000,
    10: 142913828922,
    11: 70600674,
    12: 76576500,
    13: 5537376230,
    14: 837799,
    15: 137846528820,
    16: 1366,
    17: 21124,
    18: 1074,
    19: 171,
    20: 648,
    21: 31626,
    22: 871198282,
    23: 4179871,
    24: 2783915604,
    25: 4782,
    26: 983,
    27: -59231,
    28: 669171001,
    29: 9183,
    30: 443839,
    31: 73682,
    32: 45228,
    33: 100,
    34: 40730,
    35: 55,
    36: 872187,
    37: 748317,
    38: 932718654,
    39: 840,
    40: 210,
    41: 7652413,
    42: 162,
    43: 16695334890,
    44: 5482660}


class TestSolutions(unittest.TestCase):
    """ Test Solutions to each problem_*
    """
    number_of_problems = len(SOLUTIONS.keys()) + 1

    @parameterized.expand([(i,) for i in range(1, number_of_problems)])
    def test_problem(self, problem):
        """
        For each problem import the module, capture the stdout
        and compare it to SOLUTIONS
        """
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        __import__("problems.problem_%s" % str(problem))
        sys.stdout = old_stdout
        solution = int(mystdout.getvalue())
        self.assertEqual(SOLUTIONS[problem], solution)

if __name__ == '__main__':
    unittest.main()
