#!/usr/bin/env python

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from decimal import getcontext, Decimal

MAX = 1000


def get_length(n):
    num = 1 / Decimal(n)
    digits = str(num).split(".")[1]
    if len(digits) < 1000:  # don't get those 0.25, 0.125, etc
        return 0
    # cut the 5 first digits
    digits = digits[5:]
    # 'guess' the cycle
    for i in range(2, len(digits) // 2):
        if digits[:i] == digits[i : 2 * i] == digits[2 * i : 3 * i]:
            return i
    return 0


getcontext().prec = 10000
length = {x: get_length(x) for x in range(2, MAX)}
longest = 2
for i in length:
    if length[i] > length[longest]:
        longest = i
print(longest)
