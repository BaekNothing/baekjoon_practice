length = int(input())
numberAry = [[] for _ in range(length)]
for i in range(length) :
    numberAry[i] = list(map(int, input().split()))
sumAry = [[0, 0, 0] for _ in range(length + 1)]

def findSmaller(i, j) : 
    left = (j + 1) % 3
    right = (j + 2) % 3
    if sumAry[i][left] < sumAry[i][right] :
        return left
    else :
        return right

for i in range(1, length + 1) : 
    for j in range(3) :
        index = findSmaller(i - 1, j)
        value = sumAry[i - 1][index]
        sumAry[i][j] = numberAry[i - 1][j] + value

print(min(sumAry[length][0], sumAry[length][1], sumAry[length][2]))

