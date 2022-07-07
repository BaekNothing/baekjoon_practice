h_Bit = 0
v_Bit = 0
s_Bit = 0

length = 9
ary = [[] for i in range(length)]

for i in range(length) :
    ary[i] = list(map(int, input().split()))

def setBit(h_Bit, v_Bit, s_Bit, ary, x, y) :
    for i in range(y) :
        h_Bit = h_Bit | ary[i][x]
    for i in range(x) :
        v_Bit = v_Bit | ary[y][i]
    for i in range(3) :
        for k in range(3) :
            s_Bit = s_Bit | ary[x - x % 3 + i][y - y % 3 + k]
    print(bin(h_Bit), bin(v_Bit), bin(s_Bit))

setBit(h_Bit, v_Bit, s_Bit, ary, 8, 8)
for i in range(length) :
    print(ary[i])