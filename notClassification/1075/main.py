targetNumber = int(input())
baseNumber = int(input())
counter = 0
targetNumber -= targetNumber % 100
while (targetNumber + counter) % baseNumber != 0 :
    counter += 1
print("%0.2d" % counter)