length = int(input())

casesList = [0, 1, 2, 3]
def dynamicCalculate(length) :
    if(length < 3) :
        return casesList[length]
    counter = 3
    while counter < length + 1 :
        casesList[counter % 4] = (casesList[(counter - 1) % 4] + casesList[(counter - 2) % 4]) % 15746
        counter += 1
    return casesList[length % 4]
#int에 너무 큰 숫자를 할당하려 할 경우, python은 적당한 메모리를 찾기위해 탐색하는 과정을 거치며
#이 과정에서 메모리 초과 / 시간 초과가 생길 수 있다. (O(n^2)의 시간 복잡도를 가지기 때문)
print(dynamicCalculate(length))