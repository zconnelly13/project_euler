"""
some nifty looking list comprehension
EXPR for VAR in SET if CONDITION
"""
multiples_of_3_or_5 = [x for x in range(0, 1000) if x % 3 == 0 or x % 5 == 0]
total = sum(multiples_of_3_or_5)
print total
