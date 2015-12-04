"""
Problem 25
==========

The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.

The 12th term, F(12), is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence 
to contain 1000 digits?
"""

upper_limit = 5000  # expertly chosen after glancing at my hand

def fib_generator(limit):
    current, prev = 1, 0
    for i in xrange(0, limit):
        yield current
        current, prev = current + prev, current

def fib_digit_length_generator(limit):
    for fib in fib_generator(limit):
        yield len(str(fib))

index = list(fib_digit_length_generator(upper_limit)).index(1000) + 1
print index
