length, len = input().split()
length = int(length)
len = int(len)

ary = [1 for i in range(1, len + 1)]
while ary[0] <= length :
    print(*ary)
    digit = len - 1
    ary[digit] += 1
    while digit >= 0 and  ary[digit] > length :
        digit -= 1
        ary[digit] += 1
        for i in range (digit + 1, len) :
            ary[i] = ary[digit]