import sys
from itertools import combinations

numb_len = int(input())
numb_ary = [[] for i in range(numb_len)]
for i in range(numb_len) :
    numb_ary[i] = list(map(int, sys.stdin.readline().rstrip().split(' ')))
diff = sys.maxsize

total = 0
for i in range(numb_len) :
    for k in range(numb_len) :
        total += numb_ary[i][k]

combAry = combinations(range(numb_len), numb_len // 2)
for ary in combAry :
    arySum = 0
    for num in ary :
        for i in range(numb_len) :
            arySum += numb_ary[num][i]
            arySum += numb_ary[i][num]
    diff = min(diff, abs(total - arySum))
print(diff)