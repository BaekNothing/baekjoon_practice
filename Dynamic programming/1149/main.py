length = int(input())
numberAry = [[] for _ in range(length)]
for i in range(length) :
    numberAry[i] = list(map(int, input().split()))
sumAry = [[[0,0], [0,0], [0,0]] for _ in range(length)]
sumAry[0][0] = [0, numberAry[0][0]]
sumAry[0][1] = [1, numberAry[0][1]]
sumAry[0][2] = [2, numberAry[0][2]]

for i in range(1, length) : 
    for j in range(3) :
        index = sumAry[i][j][0]
        if (numberAry[i][(index + 1) % 3] < numberAry[i][(index + 2) % 3]) :
            newIndex = (index + 1) % 3
            newValue = numberAry[i][(j + 1) % 3]
        elif (numberAry[i][(index + 1) % 3] < numberAry[i][(index + 2) % 3]) :
            newIndex = (index + 2) % 3
            newValue = numberAry[i][(index + 2) % 3]
        elif i + 1 < length :
            if (numberAry[i + 1][(index + 1) % 3] < numberAry[i + 1][(index + 2) % 3]) :
                newIndex = (index + 1) % 3
                newValue = numberAry[i][(j + 1) % 3]
            elif (numberAry[i + 1][(index + 1) % 3] < numberAry[i + 1][(index + 2) % 3]) :
                newIndex = (index + 2) % 3
                newValue = numberAry[i][(index + 2) % 3]
        else :
            newIndex = (index + 1) % 3
            newValue = numberAry[i][(index + 1) % 3]

        sumAry[i][j] = [newIndex, sumAry[i - 1][j][1] + newValue]

print(sumAry[length - 1])
print(min(sumAry[length - 1][0], sumAry[length - 1][1], sumAry[length - 1][2]))

