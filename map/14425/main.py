mapLength, compLength = input().split()

map = {}
for i in range(int(mapLength)) :
    map[input()] = 0
result = 0
for i in range(int(compLength)) :
    if input() in map :
        result += 1
print(result)


