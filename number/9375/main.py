bigLength = int(input())
bigResult = []
for i in range(bigLength) :
    length = int(input())
    def multipleAll(ary) :
        result = 1
        for i in ary :
            result *= i
        return result
    map = {}
    for i in range(length) :
        inputStr = input().split()
        if inputStr[1] not in map :
            map[inputStr[1]] = 0
        map[inputStr[1]] += 1
    ary = []
    for key, value in map.items() : 
        ary.append(value)
    result = 1
    for i in ary :
        result *= (int(i) + 1)
    bigResult.append(result - 1)

print(*bigResult, sep='\n')