from regex import R


inputNum = int(input())

result = 0
for i in range(1, inputNum + 1) :
    while i != 0 and i % 5 == 0 :
        result += 1
        i /= 5

print(result)