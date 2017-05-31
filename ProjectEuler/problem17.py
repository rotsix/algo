#!/usr/bin/env python

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

dict = {
    0    : 0,
    1    : len("one"),
    2    : len("two"),
    3    : len("three"),
    4    : len("four"),
    5    : len("five"),
    6    : len("six"),
    7    : len("seven"),
    8    : len("eight"),
    9    : len("nine"),
    10   : len("ten"),
    11   : len("eleven"),
    12   : len("twelve"),
    13   : len("thirteen"),
    14   : len("fourteen"),
    15   : len("fifteen"),
    16   : len("sixteen"),
    17   : len("seventeen"),
    18   : len("eighteen"),
    19   : len("nineteen"),
    20   : len("twenty"),
    30   : len("thirty"),
    40   : len("forty"),
    50   : len("fifty"),
    60   : len("sixty"),
    70   : len("seventy"),
    80   : len("eighty"),
    90   : len("ninety"),
    100  : len("hundred"),
    "and": len("and"),
}

def int2len(n):
    if (n%10 == 0 and n < 100) or n < 20:
        #      20
        #      twenty
        #      1
        #      one
        return dict[n]
    elif n == 1000:
        return len("onethousand")
    elif n%100 == 0:
        #      900
        #      nine            hundred
        return dict[n//100] + dict[100]
    elif n > 100:
        #      921
        #      nine                 hundred     and           twenty-one
        return int2len(n//100) + dict[100] + dict["and"] + int2len(n%100)
    else:
        #      21
        #      twenty                   one
        return int2len((n//10)*10) + int2len(n%10)

print(sum(int2len(i) for i in range(1,1001)))
