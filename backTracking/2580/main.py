import copy

_ary = [[] for i in range(9)]
original = [[] for i in range(9)]

length = 9

def setMaps(ary, y, x, verticalMap, horizontalMap, squareMap) :
    verticalMap.clear()
    horizontalMap.clear()
    squareMap.clear()
    for i in range(y) :
        verticalMap[int(ary[i][x])] = 1
    for i in range(x) :
        horizontalMap[int(ary[y][i])] = 1
    for i in range(3) :
        for j in range(3) :
            squareMap[int(ary[y - y % 3 + i][x - x % 3 + j])] = 1

def checkMaps(ary, y, x, verticalMap, horizontalMap, squareMap) :
    if int(ary[y][x]) in verticalMap :
        return False
    if int(ary[y][x]) in horizontalMap :
        return False
    if int(ary[y][x]) in squareMap :
        return False
    return True

def recursiveCellFind(ary, y, x) : 
    if y >= length :
        for i in range(length) :
            print(*ary[i])
        print("\n")
        exit()
    
    verticalMap = {}
    horizontalMap = {}
    squareMap = {}

    ary[y][x] = original[y][x]
    setMaps(ary, y, x, verticalMap, horizontalMap, squareMap)
    
    if int(ary[y][x]) == 0 :
        for i in range(1, 10) :
            ary[y][x] = int(i)
            if checkMaps(ary, y, x, verticalMap, horizontalMap, squareMap) :
                if int(x) < 8:
                    recursiveCellFind(ary, y, x + 1)
                else :
                    recursiveCellFind(ary, y + 1, 0)
            else :
                ary[y][x] = original[y][x]
    else :
        if checkMaps(ary, y, x, verticalMap, horizontalMap, squareMap) :
            if int(x) < 8 :
                recursiveCellFind(ary, y, x + 1)
            else :
                recursiveCellFind(ary, y + 1, 0)

for i in range(length) :
    _ary[i] = input().split()
original = copy.deepcopy(_ary)

recursiveCellFind(_ary, 0, 0)