mapLength, compLength = input().split()

nameMap = {}
for i in range(int(mapLength)) :
    inputName = input()
    nameMap[inputName] = (i + 1)
    nameMap[str((i + 1))] = inputName

result = ["" for i in range(int(compLength))]
for i in range(int(compLength)) :
    result[i] = nameMap[input()]

for i in range(int(compLength)) :
    print(result[i])
