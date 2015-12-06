"""
Problem 31
==========

In England the currency is made up of pound, f, and pence, p, and
there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, f1 (100p) and f2 (200p).

It is possible to make f2 in the following way:

1xf1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can f2 be made using any number of coins?
"""

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print(ways[target])
