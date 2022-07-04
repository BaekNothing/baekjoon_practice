inputString = input()
length = len(inputString)
map = {}
for i in range(int(length)) :
    for k in range(i + 1, int(length) + 1) :
        map[inputString[i:k]] = 0
print(map.__len__())