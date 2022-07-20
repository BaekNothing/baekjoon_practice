length = int(input())

result = [[0 for i in range(10)] for k in range(length)]
result[0] = [1 for _ in range(10)]
result[0][0] = 0

for i in range(1, length) :
    for k in range(10) : 
        if k == 0 :
            result[i][k] = result[i - 1][1] % 1000000000
        elif k == 9 :
            result[i][k] = result[i - 1][8] % 1000000000
        else :
            result[i][k] = (result[i - 1][k - 1] +
                            result[i - 1][k + 1]) % 1000000000

print(sum(result[length - 1]) % 1000000000)