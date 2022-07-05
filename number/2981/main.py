import math

length = int(input())
prev = 0
reary = []
for i in range(length) :
    inputNum = int(input())
    if prev != 0 :
        distance = inputNum - prev
        distance = distance if distance > 0 else -distance
        reary.append(distance)
    prev = inputNum

GCD = reary[0]
for i in range(1, reary.__len__()) :
    GCD = math.gcd(GCD, reary[i])

result = []
result = [GCD]
end = int(math.sqrt(GCD))
for i in range(2, end + 1) :
    if GCD % i == 0 :
        left = i
        right = GCD // i
        result.append(i)
        if left != right :
            result.append(GCD // i)
        end /= i
result.sort()
print(*result)