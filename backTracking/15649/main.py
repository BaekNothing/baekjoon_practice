top, length = input().split()
top = int(top)
length = int(length)
result = []

def recursive (ary, length, top) :
    if length == 0 :
        print(*ary)
        return
    for i in range(1, top + 1) :
        goflag = True
        for k in  ary :
            if k == i :
                goflag = False
                break 
        if goflag :
            recursive(ary + [i], length - 1, top)

ary = []
recursive(ary, length, top)
#print(*result, sep='\n')
