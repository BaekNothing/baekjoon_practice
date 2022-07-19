
repeat = int(input())
result = []
for _ in range(repeat) :
    length = int(input())
    ary = [1, 1, 1, 2, 2, 3]
    def dynamicCalculate(length) :
        if(length < 6) :
            return ary[length]
        counter = 6
        while counter <= length :
            ary[counter % 6] = ary[(counter - 1) % 6] + ary[(counter - 5) % 6]
            counter += 1
        return ary[length % 6]
    result.append(dynamicCalculate(length - 1))
print(*result, sep="\n")