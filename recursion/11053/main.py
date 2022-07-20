length = int(input())
numAry = list(map(int, input().split()))
resultAry = {}

resultAry[0] = [0, numAry[0]]
for i in range(1, length) :
    now = numAry[i]
    for k in range(0, i + 1) :
        if now > resultAry[k][1] :
            resultAry[i] = [k, now]
            break