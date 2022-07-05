import math

def isIn(pos, x, y, range) -> bool :
    return math.dist([pos[0], pos[1]], [x, y]) <= range

sequence : int = int(input())
result = [0 for i in range(sequence)]
for i in range(sequence) :
    inputStr = input().split()
    srcPos = [int(inputStr[0]), int(inputStr[1])]
    destPos = [int(inputStr[2]), int(inputStr[3])]
    posCount : int = int(input())
    for k in range(posCount) :
        x, y, r = input().split()
        x = int(x)
        y = int(y)
        r = int(r)
        if isIn(srcPos, x, y, r) ^ isIn(destPos, x, y, r) :
            result[i] += 1

for i in range(sequence) :
    print(result[i])