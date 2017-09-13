#!/usr/bin/env python

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?


# brute-force
def easy():
    total = 0
    # n+1, because range(n) == [0..n-1]
    for a in range(201):
        for b in range(101):
            for c in range(41):
                for d in range(21):
                    for e in range(11):
                        for f in range(6):
                            for g in range(3):
                                for h in range(2):
                                    if a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200 == 200:
                                        total += 1
                                        print(f"1p: {a}, 2p: {b}, 5p: {c}, 10p: {d}, 20p: {e}, 50p: {f}, £1: {g}, £2: {h}")

    print(total)


# smart way
def comp(n):
    res = []
    for i in range(int(n/2)+1):
        res.append([i,n-i])
    return res

cnt = []

def hard(n, i = 0):
    global cnt
    cnt.append(0)
    if i == 0:
        cnt[i] += 1
        hard(n, i+1)
    else:
        if i in [1, 2, 5, 10, 20, 50, 100, 200]:
            cnt[i] += 1
        tmp = comp(i)
        for j in range(len(tmp)):
            print(str(i) + " " + str(tmp[j]))
            if cnt[tmp[j][0]] not in [1,2,5,10,20,50,100,200]:
                cnt[i] += cnt[tmp[j][0]]
            if cnt[tmp[j][1]] not in [1,2,5,10,20,50,100,200]:
                cnt[i] += cnt[tmp[j][1]]
        if i == n:
            return
        hard(n, i+1)

hard(10)
print(cnt)
