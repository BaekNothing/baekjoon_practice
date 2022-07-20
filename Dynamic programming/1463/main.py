inputNumber = int(input())

result = [0 for _ in range(inputNumber + 1)]
result[0] = 0
result[1] = 0


for i in range(2, inputNumber + 1) :
    if i % 3 == 0 and i % 2 == 0 :
        result[i] = min(result[i // 3] + 1, result[i // 2] + 1, result[i - 1] + 1)
    elif i % 3 == 0 :
        result[i] = min(result[i // 3] + 1, result[i - 1] + 1)
    elif i % 2 == 0 :
        result[i] = min(result[i // 2] + 1, result[i - 1] + 1)
    else :
        result[i] = result[i - 1] + 1

print(result[inputNumber])