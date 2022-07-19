n, k = input().split()
n = int(n)
k = int(k)

def countFive(inputNum) :
    result = 0
    base = 5
    while inputNum >= base :
        result += inputNum // base
        base *= 5
    return result

def countTwo(inputNum) : 
    result = 0
    base = 2
    while inputNum >= base :
        result += inputNum // base
        base *= 2
    return result

five = countFive(n) - (countFive(n - k) + countFive(k))
two = countTwo(n) - (countTwo(n - k) + countTwo(k))
print(five if five <= two else two)