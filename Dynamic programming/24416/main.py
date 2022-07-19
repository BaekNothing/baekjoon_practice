
recursiveCounter = 1
def recursiveFib(n) :
    global recursiveCounter
    if n == 1 or n == 2 : 
        return 1
    else : 
        recursiveCounter += 1
        return (recursiveFib(n - 1) + recursiveFib(n - 2))

dynamicFibList = [0, 1, 1]
dynamicCounter = 0
def dynamicFib(n) : 
    global dynamicCounter
    for i in range(3, n + 1) :
        dynamicFibList.append(dynamicFibList[i - 1] + dynamicFibList[i - 2])
        dynamicCounter += 1
    return dynamicFibList[n]

number = int(input())
recursiveFib(number)
dynamicFib(number)
print(recursiveCounter)
print(dynamicCounter)