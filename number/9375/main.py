length = int(input())

map = {}
for i in range(length) :
    inputStr = input().split()
    if inputStr[1] not in map :
        map[inputStr] = 0
    map[inputStr] += 1

