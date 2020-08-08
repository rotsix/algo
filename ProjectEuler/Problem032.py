#!/usr/bin/env python

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


def ok(a, b):
    digits = str(a * b) + str(a) + str(b)
    all_digits = [str(i) for i in range(1, 10)]
    for d in digits:
        try:
            all_digits.remove(d)
        except ValueError:
            return False
    # == []
    return not all_digits


products = []
for i in range(10000):
    for j in range(10000):
        digits = str(i) + str(j) + str(i * j)
        if len(digits) < 9:
            continue
        if len(digits) > 9:
            i += 1
            j = 0
            continue
        if ok(i, j):
            products.append(i * j)

products = list(set(products))

print(sum(products))
