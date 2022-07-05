length = int(input())

def pactorial(input):
    result = 1
    for i in range(1, int(input + 1)):
        result *= i
    return int(result)

ary = []
for i in range(length):
    k, n = input().split()
    n = int(n)
    k = int(k)
    ary.append(int(pactorial(n) // ((pactorial(n - k)) * pactorial(k))))
print(*ary, sep="\n")