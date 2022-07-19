import sys
length = int(input())
numberAry = list(map(int, input().split()))
sumAry = [0 for i in range(length)]
sumAry[0] = numberAry[0]

maxValue = sumAry[0]
for i in range(1, length) :
    sumValue = sumAry[i - 1] + numberAry[i]
    if sumValue > numberAry[i] :
        sumAry[i] = sumValue
    else :
        sumAry[i] = numberAry[i]
    maxValue = max(maxValue, sumAry[i])
print(maxValue)

