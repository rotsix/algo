#!/usr/bin/env python

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

# do…while

def is_palindrome(i,j):
    while len(i) > 0:
        tmp = i.pop()
        try:
            j.remove(tmp)
        except ValueError:
            return False

    if len(i) == 0 and len(j) == 0:
        return True
    return False

def is_good(i):
    for j in range(2,7):
        if not is_palindrome(list(str(i)), list(str(i*j))):
            return False
    return True


i = 2
while not is_good(i):
    i += 1

print(i)
