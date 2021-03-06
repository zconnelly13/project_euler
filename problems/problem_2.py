"""
Problem 2
=========

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""


def fibonacci(upper_bound):
    numbers = [1, 2]
    while numbers[-1] <= upper_bound:
        numbers.append(numbers[-1]+numbers[-2])
    return numbers

numbers = fibonacci(4000000)
even_numbers = [x for x in numbers if x % 2 == 0]
total = sum(even_numbers)
print(total)
