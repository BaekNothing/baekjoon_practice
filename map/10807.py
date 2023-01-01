count = int(input())
listValue = list(map(int, input().split()))
targetValue = int(input())
result = 0
for i in listValue : 
    if (i == targetValue) :
        result += 1
print(result)