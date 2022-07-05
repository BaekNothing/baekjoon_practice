import math

length = int(input())
ary = []
for i in range(length) : 
    ary.append(int(input()))

reary = []
for i in range(length - 1) :
    if ary[i] < ary[i + 1] :
        reary.append(ary[i + 1] - ary[i])
    else :
        reary.append(ary[i] - ary[i + 1])

GCD = reary[0]
for i in range(1, reary.__len__()) :
    GCD = math.gcd(GCD, reary[i])

result = []
for i in range(2, GCD + 1) :
    if GCD % i == 0 :
        print(i, end = ' ')