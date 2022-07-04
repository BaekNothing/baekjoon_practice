cellCount = input()

def go(index, dir) :
    if (dir == -1) :
        index -= 1
        if index < 0 :
            index = 5
        return index
    elif (dir == 1) :
        index += 1
        if index > 5:
            index = 0
        return index

ary = [0 for i in range(6)]
for i in range(6) :
    inputName = input().split()
    ary[i] = int(inputName[1])

maxNum = 0
maxIndex = 0
for i in range(6) :
    if int(ary[i]) > maxNum :
        maxNum = int(ary[i])
        maxIndex = i

dir = -1 if ary[go(maxIndex, -1)] > ary[go(maxIndex, 1)] else 1

space = ary[maxIndex] * ary[go(maxIndex, dir)]
negativeSpace = ary[go(go(maxIndex, -dir), -dir)] * ary[go(go(go(maxIndex, -dir), -dir), -dir)]

print(int(space - negativeSpace) * int(cellCount))
