length = int(input())

result = [0 for _ in range(length + 1)]
result[0] = 1
result[1] = 9
for i in range(2, length + 1) :
    result[i] = (result[i - 1] * 9 - 2) % 1000000000

print(result[length])