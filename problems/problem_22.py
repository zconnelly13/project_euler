"""
Problem 22
==========

Using names.txt (see data/problem_22.names), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

from data.problem_22 import names


def score_name(name, index):
    return sum([ord(c) - 64 for c in name]) * (index + 1)

names = sorted(names)
scores = [score_name(name, index) for index, name in enumerate(names)]
print(sum(scores))
