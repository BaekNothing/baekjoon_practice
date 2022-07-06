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
    
print(countFive(n) - (countFive(n - k) + countFive(k)))
#print(int((n//5) - ((n - k)//5 + (k)//5)))