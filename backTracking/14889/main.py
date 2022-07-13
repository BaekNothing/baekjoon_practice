import sys

def readline():
    return list(map(int, sys.stdin.readline().rstrip().split(' ')))

def recursivelyFindDiffMin(Avalue, Bvalue, index, pos) :
    global diff
    if index >= numb_len :
        result = abs(Avalue - Bvalue)
        if result < diff :
            diff = result
        return

    for i in range(numb_len) :
        x = i
        y = numb_len - i - 1
        Avalue += numb_ary[x][y] + numb_ary[y][x]
        


numb_len = int(input())
numb_ary = [[] for i in range(numb_len)]
for i in range(numb_len) :
    numb_ary[i] = readline()

diff = sys.maxsize

