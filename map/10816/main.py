length = input()
map = {}
inputNum = input().split()
for i in range(int(length)) :
    try :
        map[inputNum[i]] += 1
    except Exception:
        map[inputNum[i]] = 1

length = input()
ary = [0 for i in range(int(length))]
inputNum = input().split()
for i in range(int(length)):
    try :
        ary[i] = map[inputNum[i]]
    except Exception:
        ary[i] = 0

print(*ary)
