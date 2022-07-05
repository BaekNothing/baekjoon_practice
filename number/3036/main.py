import math


length = int(input())
ary = input().split()
ary = [int(i) for i in ary]

for i in range(1, length) :
    GCD = math.gcd(ary[i], ary[0])
    print(int(ary[0] / GCD), "/", int(ary[i] / GCD), sep="")