"""
Problem 38
==========

Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by
1, 2, 3, 4, and 5, giving the pandigital, 918273645, which
is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


from tools import is_pandigital

upper_bound = 9999


def get_concatenated_product(n):
    i = 1
    concatenated_product = ""
    while len(concatenated_product) < 9:
        concatenated_product += str(n*i)
        i += 1
    return concatenated_product


pandigitals = []
for n in range(2, upper_bound):
    concatenated_product = get_concatenated_product(n)
    if len(concatenated_product) == 9 and is_pandigital(concatenated_product):
        pandigitals.append(concatenated_product)

print(max(pandigitals))
