#!/usr/bin/env python

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import gcd

def cnts(i, j):
    stri = str(i)
    strj = str(j)
    if stri[0] == str(0) or stri[1] == str(0) or strj[0] == str(0) or strj[1] == str(0):
        return [-1, -1]
    if stri[0] == strj[0]:
        return [1, 1]
    if stri[0] == strj[1]:
        return [1, 0]
    if stri[1] == strj[0]:
        return [0, 1]
    if stri[1] == strj[1]:
        return [0, 0]
    return [-1, -1]

def prod(list):
    res = 1
    for i in list:
        res *= i
    return res


nums = []
denums = []

for j in range(10,100):
    for i in range(10, j):
        common = cnts(i,j)
        if common != [-1,-1] and int(str(i)[common[0]])/int(str(j)[common[1]]) == i/j:
            #print(str(i)[common[0]] + "/" + str(j)[common[1]])
            #print(f"{i}/{j}")
            nums.append(int(str(i)[common[0]]))
            denums.append(int(str(j)[common[1]]))

prodNums = prod(nums)
prodDenums = prod(denums)

print(int(prodDenums / gcd(prodNums, prodDenums)))

