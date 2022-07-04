firstLength, secondLength = input().split()
map = {}
inputName = input().split()
for i in range(int(firstLength)) :
    map[inputName[i]] = 0

inputName = input().split()
for i in range(int(secondLength)) :
    if(inputName[i] in map) :
        map[inputName[i]] = 1
    else :
        map[inputName[i]] = 0

result = 0
for i in map :
    if map[i] == 0 :
        result += 1

print(result)