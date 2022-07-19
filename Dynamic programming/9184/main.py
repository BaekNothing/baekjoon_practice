import sys

result = []
while True:
    numbList = [[[0 for i in range(21)] for i in range(21)] for j in range(21)]
    numbList[0][0][0] = 1
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == -1 and b == -1 and c == -1 :
        break

    cal_result = 0
    if a <= 0 or b <= 0 or c <= 0 :
        cal_result = 1
    elif a > 20 or b > 20 or c > 20 :
        _a, _b, _c = 20, 20, 20
    else :
        _a, _b, _c = a, b, c
    if cal_result == 0 :
        for i in range(_a + 1) :
            for k in range (_b + 1) :
                for z in range (_c + 1) : 
                    if i <= 0 or k <= 0 or z <= 0 :
                        numbList[i][k][z] = 1
                    elif i < k and k < z :
                        numbList[i][k][z] = numbList[i][k][z - 1] + numbList[i][k - 1][z - 1] - numbList[i][k - 1][z]
                    else : 
                        numbList[i][k][z] = numbList[i - 1][k][z] + numbList[i - 1][k - 1][z] + numbList[i - 1][k][z - 1] - numbList[i - 1][k - 1][z - 1]
        cal_result = numbList[_a][_b][_c]    
    result.append(f"w({a}, {b}, {c}) = {cal_result}")
print(*result, sep='\n')