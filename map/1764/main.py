from re import X


firstLength, secondLength = input().split()
firstMap = {}
for i in range(int(firstLength)) :
    firstMap[input()] = 1

result = []
for i in range(int(secondLength)) :
    inputName = input()
    try :
        if (firstMap[inputName] == 1) :
            result.append(inputName)
    except KeyError :
        pass
result.sort()
print(result.__len__())
for i in range(result.__len__()) :
    print(result[i])