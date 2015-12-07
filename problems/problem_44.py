"""
Problem 44
==========

Pentagonal numbers are generated by the formula, P(n)=n(3n-1)/2.
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
However, their difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk,
for which their sum and difference are pentagonal and D = |Pk - Pj|
is minimised; what is the value of D?
"""


pentagonal_numbers = {n*(3*n-1)/2: True for n in range(1, 5000)}
pentagonal_pairs = [
        (j, k)
        for j in pentagonal_numbers
        for k in pentagonal_numbers
        if pentagonal_numbers.get(abs(j-k)) and
        pentagonal_numbers.get(j+k)]

differences = map(lambda x: abs(x[0]-x[1]), pentagonal_pairs)
print(min(differences))
