import string

length = input()
array = [["" for i in range(2)] for j in range(int(length))]
for i in range(int(length)) :
    inputValue = input().split()
    array[i] = [inputValue[0], inputValue[1]]
array.sort(key=lambda x: int(x[0]))

for i in range(int(length)) :
    print(array[i][0], array[i][1])