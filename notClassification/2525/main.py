Hour, Min = map(int, input().split())
Time = int(input())

Hour = Hour + Time // 60
Min = Min + Time % 60
if (Min >= 60) :
    Min -= 60
    Hour += 1
Hour = Hour % 24
print(Hour, Min)