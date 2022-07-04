cellCount = input()

loop = [4, 2, 3, 1]
map = {}

firstInput = input().split()
index = 0
breakIndex = 0
while loop[index] != int(firstInput[0]) :
    index += 1
    if index == 4 :
        index = 0
prevInput = firstInput[1]

map[int(firstInput[0])] = firstInput[1]
negativeSpace = 0
inputName = [0, 0]
while True :
    try :
        inputName = input().split()
        index += 1
        if int(index) == 4 :
            index = 0
        if (int(loop[int(index)]) != int(inputName[0])) and negativeSpace == 0:
            negativeSpace = int(prevInput) * int(inputName[1])
            breakIndex = index
        prevInput = inputName[1]
        map[int(inputName[0])] = inputName[1]
    except :
        break

if negativeSpace == 0 :
    negativeSpace = int(firstInput[1]) * int(inputName[1])
    breakIndex = index

space = int(map[loop[int(breakIndex)]]) * int(map[loop[int((breakIndex + 1) if (breakIndex + 1) < 4 else 0)]]) - negativeSpace
print (space * int(cellCount))