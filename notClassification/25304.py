totalValue = int(input())
count = int(input())
resultValue = 0
for i in range(count) : 
    inputValue = list(map(int, input().split()))
    resultValue += inputValue[0] * inputValue[1]
print("Yes" if totalValue == resultValue else "No")