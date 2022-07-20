N = input().split()
N = [int(i) for i in N]

if (N[0] == N[1] == N[2]) :
    print(10000 + N[0] * 1000)
elif (N[0] == N[1]) :
    print(1000 + N[0] * 100)
elif (N[0] == N[2]) :
    print(1000 + N[0] * 100)
elif (N[1] == N[2]):
    print(1000 + N[1] * 100)
else :
    print(max(N) * 100)
