length = int(input())

ary = []
for _ in range(length):
    ary.append(int(input()))

result = [[0, 0, 0] for _ in range(length)]
result[0] = [0, ary[0], 0]


def findMax(index):
    result[index][0] = max(result[index - 1][0], result[index - 1][1], result[index - 1][2])
    result[index][1] = result[index - 1][0] + ary[index]
    result[index][2] = result[index - 1][1] + ary[index]


for i in range(1, length):
    findMax(i)

final = max(result[length - 1][0], result[length - 1][1], result[length - 1][2])

semiFinal =  0
if (length > 1) :
 semiFinal = max(result[length - 2][0], result[length - 2][1], result[length - 2][2])

print(max(final, semiFinal))