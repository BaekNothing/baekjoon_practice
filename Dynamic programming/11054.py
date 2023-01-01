def findMaxIncreaseIndex(increaseList : list, targetList : list, targetIndex : int) -> int :
    maxIndex = 0
    maxValue = -1
    for i in range(targetIndex) : 
        if (targetList[i] < targetList[targetIndex] 
            and maxValue < increaseList[i]) : 
            maxIndex = i
            maxValue = increaseList[i]
    return maxIndex 

def findMaxDecreaseIndex(decreaseList : list, targetList : list, count : int, targetIndex : int) -> int :
    maxIndex = count - 1
    maxValue = -1
    for i in reversed(range(targetIndex + 1, count)) : 
        if (targetList[i] < targetList[targetIndex] 
            and maxValue < decreaseList[i]) : 
            maxIndex = i
            maxValue = decreaseList[i]
    return maxIndex 

count = int(input())
listValue = list(map(int, input().split()))
listIncrease = [0 for i in range(count)]
listDecrease = [0 for i in range(count)]

for i in range(1, count):
    increaseIndex = findMaxIncreaseIndex(listIncrease, listValue, i)
    if(listValue[i] > listValue[increaseIndex]) :
        listIncrease[i] = listIncrease[increaseIndex] + 1
    decreaseIndex = findMaxDecreaseIndex(listDecrease, listValue, count, count - 1 - i)
    if(listValue[count - 1 - i] > listValue[decreaseIndex]) :
        listDecrease[count - 1 - i] = listDecrease[decreaseIndex] + 1

maxValue = 0
for i in range(count) :
    sumBoth = listDecrease[i] + listIncrease[i]
    if (sumBoth > maxValue) :
        maxValue = sumBoth
print(maxValue + 1)