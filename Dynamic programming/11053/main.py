length = int(input())
inputAry = list(map(int, input().split()))

# [head, length]
cashAry = [[0,0] for _ in range(length)]
cashAry[0] = [inputAry[0], 1]
for i in range(1, length):
    maxLength = 0
    maxPos = 0
    for j in range(i):
        if inputAry[i] > cashAry[j][0] :
            maxLength = max(cashAry[j][1], maxLength)
            maxPos = j
    cashAry[i] = [inputAry[i], maxLength + 1]
#print(*cashAry, sep='\n')
print(max(cashAry[i][1] for i in range(length)))