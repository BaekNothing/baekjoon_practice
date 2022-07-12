import sys
from copy import deepcopy

def readLineStr() :
    return list(map(int, sys.stdin.readline().rstrip().split(' ')))

def calculate(flag, x, y) : 
    if flag == '+' : 
        return x + y
    elif flag == '-' : 
        return x - y
    elif flag == '*' : 
        return x * y
    elif flag == '/' : 
        return x // y
    else : 
        return 0

# * > + > - > /
def setMax(flag) : 
    ary_diff_max = 0
    maxPos = 0
    for i in range(aryLength - 1) : 
        if signAry[i] == 0 and ary_diff_max < calculate(flag, ary[i], ary[i + 1]): 
            ary_diff_max = abs(ary[i] - ary[i + 1])
            maxPos = i
    return maxPos

def setMin(flag) : 
    ary_diff_min = sys.maxsize
    minPos = 0
    for i in range(aryLength - 1) : 
        if signAry[i] == 0 and ary_diff_min > calculate(flag, ary[i], ary[i + 1]): 
            ary_diff_min = abs(ary[i] - ary[i + 1])
            minPos = i
    return minPos

def getResult(ary, sign) : 
    result = calculate(sign[0], ary[0], ary[1])
    del ary[1]
    for i in range(1, len(ary)) : 
        calculate(sign, result, ary[i])
    return result

aryLength = int(input())
ary = readLineStr()
resultAry = deepcopy(ary)
plus, minus, multiple, divide = readLineStr()
signAry = ['' for i in range(aryLength - 1)]

for i in range(multiple) : 
    signAry[setMax('*')] = '*'
for i in range(plus) : 
    signAry[setMax('+')] = '+'
for i in range(minus) : 
    signAry[setMax('-')] = '-'
for i in range(divide) :
    signAry[setMax('/')] = '/'

print(*signAry)