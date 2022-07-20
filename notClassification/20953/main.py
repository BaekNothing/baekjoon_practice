length = int(input())

def dolmen(a, b) :
    return ((a + b) ** 2 * (a + b - 1)) // 2

result = []
for _ in range(length):
    a, b = map(int, input().split())
    result.append(dolmen(a, b))

print(*result, sep='\n')

