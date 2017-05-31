#!/usr/bin/env python

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(nbr):
    nbr = str(nbr)
    for i in range(len(nbr)//2):
        if nbr[i] != nbr[len(nbr)-1 - i]:
            return False
    return True

max = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        if palindrome(i*j) is True:
            if i*j > max:
                max = i*j

print(max)

