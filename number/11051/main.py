n, k = input().split()
n = int(n)
k = int(k)

def pactorial(input) :
    result = 1
    for  i in range(1, int(input + 1)) :
        result *= i
    return int(result)

print(int(pactorial(n) // ((pactorial(n - k) * pactorial(k))) % 10007))