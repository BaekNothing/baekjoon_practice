import os

COUNT = 6
inputVars = list(map(int, input().split()))
baseVars = [1, 1, 2, 2, 2, 8]
resultVars = [0, 0, 0, 0, 0, 0,]
for i in range(COUNT) :
    resultVars[i] = baseVars[i] - inputVars[i]
print(*resultVars, sep=' ')