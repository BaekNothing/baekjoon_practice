length = input()
mapAry = [0 for i in range(-10000042, 10000042)]
mapInput = input().split()
for i in mapInput :
    mapAry[int(i)] += 1

length = input()
cardAry = [0 for i in range(int(length))]
cardAry = input().split()

for i in range(int(length)) :
    if mapAry[int(cardAry[i])] == 0 :
        cardAry[i] = 0
    else :
        cardAry[i] = 1
print(*cardAry)