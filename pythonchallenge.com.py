#!/usr/bin/env python

def e1():
    # http://www.pythonchallenge.com/pc/def/0.html
    print(2**38)

def e2():
    # http://www.pythonchallenge.com/pc/def/map.html
    text="""g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
    for i in text:
        if i != ' ':
            char = (ord(i) + 2 - ord('a'))%26 + ord('a')
            print(chr(char), end='')
        else:
            print(" ", end='')

    print("\n")

    for i in "map":
        print(chr(ord(i) + 2), end='')

    # real solution:
    # table = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
    # string.translate(text, table)
    # or text.translate(table)

import urllib3
def e3():
    # http://www.pythonchallenge.com/pc/def/ocr.html
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.pythonchallenge.com/pc/def/ocr.html')
    html = r.data

    print(html)

e3()

