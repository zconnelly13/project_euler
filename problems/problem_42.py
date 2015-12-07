"""
Problem 42
==========

The nth term of the sequence of triangle numbers is given by,
t(n) = (1/2)n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t(10).
If the word value is a triangle number
then we shall call the word a triangle word.

Using words.txt (data/problem_42.words) how many are triangle words?
"""

from data.problem_42 import words


def score_word(word):
    return sum([ord(c) - 64 for c in word])

scores = [float(score_word(word)) for word in words]
triangle_numbers = [
    (0.5)*n*(n+1)
    for n in range(0, 21)]

number_of_triangle_words = len([
    True for score in scores
    if score in triangle_numbers])
print(number_of_triangle_words)
