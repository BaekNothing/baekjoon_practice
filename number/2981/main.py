import math

from numpy import append

length = int(input())
ary = []
for i in range(length) : 
    ary.append(int(input()))
ary.sort()

reary = []
for i in range(length - 1) :
    reary.append(ary[i + 1] - ary[i])

GCD = reary[0]
for i in range(1, reary.__len__()) :
    GCD = math.gcd(GCD, reary[i])

result = []
for i in range(2, GCD + 1) :
    if GCD % i == 0 :
        result.append(i)

print(*result)