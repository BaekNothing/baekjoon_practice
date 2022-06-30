length = input()

array = [0 for i in range(int(length))]
array = input().split()

copyArray = array.copy()
copyArray.sort(key=lambda x: int(x))

dictionary = {}
counter = 0
for i in range(int(copyArray.__len__())) :
    if copyArray[i] not in dictionary :
        dictionary[copyArray[i]] = counter
        counter += 1

for i in range(int(length)) :
    array[i] = dictionary[array[i]]
print(*array)