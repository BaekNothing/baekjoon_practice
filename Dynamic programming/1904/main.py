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
#int�� �ʹ� ū ���ڸ� �Ҵ��Ϸ� �� ���, python�� ������ �޸𸮸� ã������ Ž���ϴ� ������ ��ġ��
#�� �������� �޸� �ʰ� / �ð� �ʰ��� ���� �� �ִ�. (O(n^2)�� �ð� ���⵵�� ������ ����)
print(dynamicCalculate(length))