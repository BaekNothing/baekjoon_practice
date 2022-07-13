import sys

def readLineStr() :
    return list(map(int, sys.stdin.readline().rstrip().split(' ')))

def calculate(input, a, b) :
    if input == 0 :
        return a + b
    elif input == 1 : 
        return a - b
    elif input == 2 :
        return a * b
    elif input == 3 :
        return int(a / b)

aryLength = int(input())
numbAry = readLineStr()
signAry = readLineStr()

maxValue = -1 * sys.maxsize - 1
minValue = sys.maxsize

def recursivelyFind(result, index) :
    global maxValue, minValue
    if index >= aryLength :
        if result > maxValue :
            maxValue = result
        if result < minValue :
            minValue = result
        return 
    
    for i in range(4) :
        if signAry[i] <= 0 :
            continue
        signAry[i] -= 1
        recursivelyFind(calculate(i, result, numbAry[index]), index + 1)
        signAry[i] += 1
        
recursivelyFind(numbAry[0], 1)
print(maxValue, minValue, sep='\n')