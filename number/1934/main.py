length = int(input())

result = []
for i in range(length) : 
    inputStr = input().split()
    first = int(inputStr[0])
    second = int(inputStr[1])
    if first < second :
        temp = first
        first = second
        second = temp
    elif first == second :
        result.append(first)
        continue

    dust = first % second
    followNumber = second
    while True :
        if dust == 0 or followNumber % dust == 0 :
            result.append(int(first * second / (dust if dust != 0 else followNumber)))
            break
        temp = dust
        dust = followNumber % dust
        followNumber = temp   

for i in range(result.__len__()) :
    print(int(result[i]))
