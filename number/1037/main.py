length = int(input())
ary = []
inputName = input().split()
for i in range(length) : 
    ary.append(int(inputName[i]))
ary.sort()

print(ary[0] * ary[length - 1])