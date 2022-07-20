length = int(input())

numAry = [[] for _ in range(length)]
for i in range(length) :
    numAry[i] = list(map(int, input().split()))
sumAry = [[0 for _ in range(i + 1)] for i in range(length)]
sumAry[0] = numAry[0]

def findBigger(i, j) :
    left = j - 1 if (j - 1) >= 0 else 0
    right = j if j < i else i
    #print("left:", sumAry[i][left], "right:", sumAry[i][right])
    if sumAry[i][left] >= sumAry[i][right] :
        return left
    else :
        return right

for i in range(1, length) :
    for k in range(i + 1):
        index = findBigger(i - 1, k)
        sumAry[i][k] = sumAry[i - 1][index] + numAry[i][k]
        #print(sumAry[i][k], "=", sumAry[i - 1][index], "+", numAry[i][k], sep="")
    #print(sumAry[i])
#print(sumAry[length - 1])
print(max(sumAry[length - 1]))