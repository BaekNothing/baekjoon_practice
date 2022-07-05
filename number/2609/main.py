inputStr = input().split()
first = int(inputStr[0])
second = int(inputStr[1])

if first == second :
    print(first)
    print(first)
    exit()

ary = []
max = first if first > second else second
i = 2
while True :
    if i > max :
        break
    if first % i == 0 and second % i == 0 :
        first /= i
        second /= i
        ary.append(i)
    if first % i != 0 or second % i != 0 :
        i += 1

result = 1
for i in range(ary.__len__()) :
    result *= ary[i]

print(int(result))
print(int(result * first * second))