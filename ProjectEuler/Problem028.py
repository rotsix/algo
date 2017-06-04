#!/usr/bin/env python

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def diags(maximum, n=0, local_max=0):
    if n == maximum:
        sum = 0
        for i in range(4):
            local_max += n*2
            sum += local_max
        return sum
    if n == 0:
        return 1 + diags(maximum, n+1, 1)
    else:
        sum = 0
        for i in range(4):
            local_max += n*2
            sum += local_max
        return sum + diags(maximum, n+1, local_max)
        
print(diags(1001//2))
