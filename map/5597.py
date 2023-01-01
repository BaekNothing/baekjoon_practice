listValue = [0 for i in range(30)]
resultValue = [0, 0]

for i in range(28) :
    listValue[int(input()) - 1] = 1
for i in range(30) :
    if(listValue[i] == 0) :
        if(resultValue[0] == 0) :
            resultValue[0] = i + 1
        else :
            resultValue[1] = i + 1

print(*resultValue, sep='\n')