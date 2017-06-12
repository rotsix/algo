#!/usr/bin/env python

# The decimal number, 585 = 1001001001₂ (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

total = 0

for i in range(1_000_000):
    stri = str(i)
    strbini = str(bin(i))[2:]
    if stri == stri[::-1] and strbini == strbini[::-1]:
        total += i

print(total)
