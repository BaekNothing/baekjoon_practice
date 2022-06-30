length = input()
cols = 2
rows = int(length)
arr = [[0 for c in range(cols)] for r in range(rows)]
for i in range(0, int(length)):
    arr[i] = list(map(int, input().split()))

arr.sort(key=lambda x: (x[1], x[0]))
for i in range(0, int(length)):
    print(arr[i][0], arr[i][1])